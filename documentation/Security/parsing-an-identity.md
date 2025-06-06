# Parsing an Identity

**Framework**: Security

Extract the private key and certificate from an identity.

#### Overview

After you have an identity, you can extract the private key from it with a call to the [`SecIdentityCopyPrivateKey(_:_:)`](secidentitycopyprivatekey(_:_:).md) function:

Similarly, you can extract the certificate with a call to the [`SecIdentityCopyCertificate(_:_:)`](secidentitycopycertificate(_:_:).md) function:

In both cases, you inspect the returned status value to determine whether an error occurred during the extraction. In Objective-C, you are responsible for freeing the associated memory with a call to [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) when you’re done with these objects. In Swift, the system manages the memory automatically, releasing it when the object goes out of scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/parsing-an-identity)*