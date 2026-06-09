# Managing certificates for device management services and devices

**Framework**: Device Management

Ensure secure connectivity with your device management service using valid certificates.

#### Overview

With device management, devices can only connect to services that have valid SSL certificates. If your device management serviceʼs SSL certificate roots to your organizationʼs root certificate, a device must trust the root certificate before it can connect to your service.

Include the root certificate and any intermediate certificates in the same profile that contains the MDM payload. Certificate payloads install before the MDM payload.

It’s possible to install a trust profile before installing the enrollment profile that contains the MDM payload. If your device management service uses separate trust profiles for SSL trust, set the `trust_profile_url` value as described in [`Providing information about your device management service`](providing-information-about-your-device-management-service.md).

Replace the profile that contains your MDM payload before any of the certificates in that profile expire.

> ⚠️ **Warning**:  If any certificate in the SSL trust chain expires, the device can’t connect to the device management service to receive its commands. When this occurs, you lose the ability to manage that device.

A device management service identifies a connecting device by examining the deviceʼs identity certificate. The service then cross-checks the `UDID` in the message to ensure there’s an association between the `UDID` and the certificate.

The system uses the deviceʼs identity certificate to establish the SSL/TLS connection to the device management service.

#### Deliver Identity Certificates to Devices

Each device must have a unique identity certificate. Deliver these certificates using the Automated Certificate Management Environment (ACME) which is recommended, Simple Certificate Enrollment Protocol (SCEP), or as PKCS#12 containers. Using ACME or SCEP is advantageous because these protocols help ensure that the private key for the identity exists on the device only.

Consult your organizationʼs public key infrastructure policy to determine which method is appropriate for your installation.

#### Pass a Device Identity Certificate Through a Proxy

If your device management service sits behind a proxy that strips away or doesn’t ask for an identity certificate, you can pass the device’s identity through a proxy. If the value of the `SignMessage` field in the MDM payload is `true`, each message that comes from the device carries an additional HTTP header named `Mdm-Signature`. This header contains a Base64-encoded CMS detached signature of the message.

Your service validates the body of the message with the detached signature in the `SignMessage` header. If the validation is successful, the message is from the signer of the certificate in the signature.

> 💡 **Tip**:  Only use this option if necessary because it adds approximately 2 kilobytes of data to each message.

## See Also

- [Managing connections](managing-connections.md)
  Establish or remove a connection between a device and your device management service.
- [Providing information about your device management service](providing-information-about-your-device-management-service.md)
  Create a service configuration entry point to your device management service to access frequently used information.
- [Dealing with inactive managed devices and invalid push tokens](dealing-with-inactive-managed-devices-and-invalid-push-tokens.md)
  Handle when devices become unmanageable due to inactivity or invalid push tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managing-certificates-for-device-management-services-and-devices)*