# Examining a Certificate

**Framework**: Security

Learn how to retrieve properties from a certificate.

#### Overview

In order to fulfill its purpose of verifying the identity of its owner, a certificate contains such information as:

- The certificate issuer
- The certificate holder
- A validity period (the certificate isn’t valid before or after this period)
- The public key of the certificate’s owner
- , which contain additional information such as alternative names for the certificate holder and allowable uses for the private key associated with the certificate
- A digital signature from the certification authority to ensure that the certificate hasn’t been altered and to indicate the identity of the issuer

The certificate, key, and trust services API provides functions to examine the properties of a certificate. For example, the [`SecCertificateCopySubjectSummary(_:)`](seccertificatecopysubjectsummary(_:).md) function returns a human readable summary of the certificate:

In macOS, there are a few additional functions that return data about a certificate. For example, to pull the public key from a certificate, you use the [`SecCertificateCopyPublicKey(_:)`](seccertificatecopypublickey(_:_:).md) function:


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/examining-a-certificate)*