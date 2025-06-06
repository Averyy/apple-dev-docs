# Creating an Identity

**Framework**: Security

Create an identity from a certificate and private key.

#### Overview

In macOS, you can create an identity as a combination of a certificate and a private key. You begin by obtaining a certificate reference in one of the ways described in [`Getting a Certificate`](getting-a-certificate.md). You then supply that reference to the [`SecIdentityCreateWithCertificate(_:_:_:)`](secidentitycreatewithcertificate(_:_:_:).md) function:

The function attempts to locate the corresponding private key in the default keychain list or in the keychain or keychains that you specify as the first argument. If it succeeds, as indicated by the status result, it populates the identity reference with a pointer to a newly created identity object. Otherwise, the identity reference remains empty.

To persist a copy of the identity for later use, store it in the keychain, as described in [`Storing an Identity in the Keychain`](storing-an-identity-in-the-keychain.md).

In Objective-C, when you are done with the identity, you are responsible for freeing the object’s memory. In Swift, the system manages the object’s memory automatically, releasing it when the object goes out of scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/creating-an-identity)*