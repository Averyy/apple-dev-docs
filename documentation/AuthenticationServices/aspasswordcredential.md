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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [ASAuthorizationCredential](asauthorizationcredential.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Password AutoFill](../Security/password-autofill.md)
  Streamline your app’s login and onboarding procedures.
- [class ASAuthorizationPasswordProvider](asauthorizationpasswordprovider.md)
  A mechanism for generating requests to perform keychain credential sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasswordcredential)*