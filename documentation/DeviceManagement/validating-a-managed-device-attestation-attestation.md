# Validating a Managed Device Attestation

**Framework**: Device Management

Verify an attestation that a managed device returns by performing the required steps.

#### Overview

The [`Managed Device Attestation`](https://developer.apple.comhttps://support.apple.com/guide/deployment/dep28afbde6a) feature provides a cryptographic declaration of device properties that you can use as part of a trust evaluation. This feature helps protect against various threats, such as a compromised device providing false information.

You can use Managed Device Attestation in two different workflows:

- Device information attestation, requested using the [`Device Information`](device-information-command.md) command
- ACME attestation, requested as part of an ACME certificate enrollment

In both cases, you need to carefully validate the attestation to preserve the security assurances of Managed Device Attestation. The validation requirements differ between the two workflows, as outlined below.

#### Validate a Device Information Attestation

When your device management service sends a [`Device Information`](device-information-command.md) command that requests an attestation, the response’s `DevicePropertiesAttestation` key has a value that is a chain of certificates with the leaf certificate first. The leaf certificate describes the properties of an Apple device and may differ depending on the device type.

To properly validate the attestation, follow these steps in order:

1. Verify that there’s a valid chain of certificate issuers from the leaf to the Apple Enterprise Attestation Root CA. This CA isn’t provided in the response, but is available from the [`Apple Private PKI Repository`](https://developer.apple.comhttps://www.apple.com/certificateauthority/private/). If the leaf certificate doesn’t chain to this CA, the attestation isn’t trustworthy. There’s no scenario during normal operations in which this validation step fails. You can choose to ignore the attestation entirely, or flag it as an incident that needs investigation.
2. If the [`Device Information`](device-information-command.md) request includes a value for the `DeviceAttestationNonce` key, verify that it matches the freshness code in the leaf certificate. If the freshness code doesn’t match, the attestation wasn’t generated in response to the request, so dynamic properties in the attestation may be out of date. See the `DeviceAttestationNonce` key for details of attestation caching, which may affect the expected value.
3. Parse out the device properties in the various OIDs in the leaf certificate and evaluate their values. Any missing OIDs or blank values indicate that Apple’s attestation servers were unable to reliably determine the corresponding property.

#### Validate an Acme Attestation

When the device installs a [`ACMECertificate`](acmecertificate.md) payload or [`AssetCredentialACME`](assetcredentialacme.md) declaration asset that has its `Attest` key set to true, the device requests an attestation from Apple’s attestation servers. Your ACME server receives the attestation certificate chain when the device responds to the `device-attest-01` challenge.

To properly validate the attestation, follow these steps in order:

1. Verify that there’s a valid chain of certificate issuers from the leaf to the Apple Enterprise Attestation Root CA. This CA isn’t provided in the response, but is available from the [`Apple Private PKI Repository`](https://developer.apple.comhttps://www.apple.com/certificateauthority/private/). If the leaf certificate doesn’t chain to this CA, the attestation isn’t trustworthy. There’s no scenario during normal operations in which this validation step fails. You can choose to ignore the attestation entirely, or flag it as an incident that needs investigation.
2. Perform any custom validation of the public key in the leaf certificate. This is the public key of the identity this ACME flow generates. For example, an organization may require a particular key type or key size. Also check the key against other issued certificates to detect unexpected key reuse.
3. Calculate the SHA-256 hash of the `token` that your ACME solution sent to the device in the `device-attest-01` challenge. Verify that this hash matches the freshness code in the leaf certificate. If the freshness code doesn’t match, there’s no evidence that the attestation was generated specifically for this challenge, meaning dynamic properties in the attestation may be out of date.
4. Parse out the device properties in the various OIDs in the leaf certificate and evaluate their values. Any missing OIDs or blank values indicate that Apple’s attestation servers were unable to reliably determine the corresponding device property.
5. Perform any custom validation of the device properties. This can include verifying that the persistent device identifiers (serial number and UDID) match expected values for a device the organization manages, that the device’s security posture meets requirements, and that the installed software versions meet minimum requirements.
6. Retain the public key in the attestation leaf certificate for a later validation.

Once all these validation steps succeed, your ACME server can proceed to the `finalize` phase of the ACME protocol. Verify that the public key in the certificate signing request (CSR) sent to your ACME server is identical to the public key in the leaf certificate of the attestation. The public key in the attestation in turn matches the attested key. This provides a chain of trust from the CSR back to the hardware-bound private key. The public key of the CSR and the public key in the leaf certificate must have the same type, size, and raw bytes. If this validation fails, you have no evidence that the key for the issued certificate is hardware-bound, or that the requesting device has the attested properties. In this case, your ACME server needs to respond with a `badCSR` error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/validating-a-managed-device-attestation-attestation)*