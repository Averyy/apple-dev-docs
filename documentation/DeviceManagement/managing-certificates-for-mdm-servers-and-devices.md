# Managing Certificates for MDM Servers and Devices

**Framework**: Device Management

Ensure secure MDM connectivity with valid certificates.

#### Overview

In MDM, devices can only connect to servers that have valid SSL certificates. If your MDM serverʼs SSL certificate roots to your organizationʼs root certificate, a device must trust the root certificate before it can connect to your server.

Include the root certificate and any intermediate certificates in the same profile that contains the MDM payload. Certificate payloads install before the MDM payload.

It’s possible to install a trust profile before installing the enrollment profile that contains the MDM payload. If your MDM server uses separate trust profiles for SSL trust, set the `trust_profile_url` value as described in [`Simplifying MDM Server Administration for iOS Devices`](simplifying-mdm-server-administration-for-ios-devices.md).

Replace the profile that contains your MDM payload before any of the certificates in that profile expire.

> ⚠️ **Warning**:  If any certificate in the SSL trust chain expires, the device can’t connect to the MDM server to receive its commands. When this occurs, you lose the ability to manage that device.

An MDM server identifies a connecting device by examining the deviceʼs identity certificate. The server then cross-checks the `UDID` in the message to ensure there’s an association between the `UDID` and the certificate.

The system uses the deviceʼs identity certificate to establish the SSL/TLS connection to the MDM server.

##### Deliver Identity Certificates to Devices

Each device must have a unique identity certificate. Deliver these certificates as PKCS#12 containers or by using the Simple Certificate Enrollment Protocol (SCEP). Using SCEP is advantageous because the protocol ensures that the private key for the identity exists on the device only.

Consult your organizationʼs public key infrastructure policy to determine which method is appropriate for your installation.

##### Pass an Identity Certificate Through a Proxy

If your MDM server sits behind a proxy that strips away or doesn’t ask for an identity certificate, you can pass the device’s identity through a proxy. If the value of the `SignMessage` field in the MDM payload is `true`, each message that comes from the device carries an additional HTTP header named `Mdm-Signature`. This header contains a Base64-encoded CMS detached signature of the message.

Your server validates the body of the message with the detached signature in the `SignMessage` header. If the validation is successful, the message is from the signer of the certificate in the signature.

> 💡 **Tip**:  Only use this option if necessary because it adds approximately 2 kilobytes of data to each message.

## See Also

- [Deploying MDM Enrollment Profiles](deploying-mdm-enrollment-profiles.md)
  Choose the technique to deploy MDM enrollment profiles for your organization.
- [Installing Profiles on Devices](installing-profiles-on-devices.md)
  Optimize deployment of profiles and provisioning profiles.
- [Setting Up Push Notifications for Your MDM Customers](setting-up-push-notifications-for-your-mdm-customers.md)
  Create and sign a certificate signing request (CSR) to enable push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managing-certificates-for-mdm-servers-and-devices)*