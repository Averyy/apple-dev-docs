# ASPasswordCredential

**Framework**: Authentication Services  
**Kind**: class

A password credential.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class ASPasswordCredential
```

## Topics

### Creating a credential
- [init(user: String, password: String)](aspasswordcredential/init(user:password:).md)
  Initializes a password credential.
### Accessing the username and password
- [var user: String](aspasswordcredential/user.md)
  The user for a password credential object.
- [var password: String](aspasswordcredential/password.md)
  The password for a password credential object.
### Initializers
- [init?(coder: NSCoder)](aspasswordcredential/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [ASAuthorizationCredential](asauthorizationcredential.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Password AutoFill](../security/password-autofill.md)
  Streamline your app’s login and onboarding procedures.
- [class ASAuthorizationPasswordProvider](asauthorizationpasswordprovider.md)
  A mechanism for generating requests to perform keychain credential sharing.
- [Password use in web browsers](password-use-in-web-browsers.md)
  Register and authenticate website users by using passwords.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasswordcredential)*