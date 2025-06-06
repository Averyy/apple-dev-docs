# Getting a Certificate

**Framework**: Security

Obtain a certificate from an identity, from DER-encoded data, or from the keychain.

#### Overview

You use functions of the certificate, key, and trust services API to manage and manipulate certificates. The API defines the [`SecCertificate`](seccertificate.md) opaque type to hold certificate objects. You typically use such an object to indicate the certificate to use for a particular cryptographic operation, such as evaluating trust. How you get a certificate reference depends on where the certificate is stored or how it’s provided to you. For example, it might come from any of the following:

-  When you read an identity from a password-protected file or from the keychain (as described in [`Importing an Identity`](importing-an-identity.md) and [`Storing an Identity in the Keychain`](storing-an-identity-in-the-keychain.md), respectively), you can extract the certificate it contains (see [`Parsing an Identity`](parsing-an-identity.md)). In macOS, you can also store a certificate in an identity along with its associated private key (see [`Creating an Identity`](creating-an-identity.md)).
-  You can export a certificate as DER-encoded data that you then store on disk or send through the network. Similarly, you can restore a certificate from this kind of data. See [`Storing a DER-Encoded X.509 Certificate`](storing-a-der-encoded-x-509-certificate.md) for details.
-  Just as with keys and passwords, you can store a certificate in a keychain and later retrieve it from there. See [`Storing a Certificate in the Keychain`](storing-a-certificate-in-the-keychain.md) for details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/getting-a-certificate)*