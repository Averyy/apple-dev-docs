# Certificate, Key, and Trust Services

**Framework**: Security

Establish trust using certificates and cryptographic keys.

#### Overview

The certificate, key, and trust services API is a collection of functions and data structures that you use to conduct secure and authenticated data transactions. Specifically, you use this API to manage and use:

-  A certificate is a collection of data that identifies its owner in a tamper-evident way. When you use a certificate to distribute a public key, a receiver can be confident of its origin. You can also package a certificate together with its corresponding private key in an identity object that you keep secret.
-  When you receive a certificate, before you can use the embedded public key, you have to answer the question, “Can I trust this certificate?” You conduct an evaluation of trust according to a set of criteria, or a trust policy.
-  After you have a key whose origin you trust, you can begin to conduct cryptographic operations, such as encryption or data signing and verification. These operations in turn typically serve a larger purpose, such as authenticating a user, transmitting data securely, or verifying that a block of data is unaltered since being sealed with a signature.

> **Note**:  Rely on the classes of the [`Security Interface`](https://developer.apple.com/documentation/SecurityInterface) framework to ensure a consistent experience when displaying certificates and trust settings to the user and when the user chooses among identities or modifies keychain settings.

 Rely on the classes of the [`Security Interface`](https://developer.apple.com/documentation/SecurityInterface) framework to ensure a consistent experience when displaying certificates and trust settings to the user and when the user chooses among identities or modifies keychain settings.

## Topics

### API Components
- [Certificates](certificates.md)
  Manage digital certificates.
- [Keys](keys.md)
  Generate, store, and use cryptographic keys.
- [Identities](identities.md)
  Combine certificates and cryptographic keys into identities.
- [Policies](policies.md)
  Obtain policies for establishing trust.
- [Trust](trust.md)
  Evaluate trust based on a given policy.
### Thread Safety
- [Working with Concurrency](working-with-concurrency.md)
  Learn about thread safety issues related to the certificate, key, and trust services API.

## See Also

- [Cryptographic Services Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011172)
- [Security Interface](../SecurityInterface/SecurityInterface.md)
  Provide user interface elements for security features such as authorization, access to digital certificates, and access to items in keychains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/certificate-key-and-trust-services)*