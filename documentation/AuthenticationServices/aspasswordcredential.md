# ASPasswordCredential

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASPasswordCredential : NSObject
```

## Topics

### Creating a credential
- [init(user: String, password: String)](./aspasswordcredential/init%28user,password%29.md)
  Initializes a password credential.
- [+ credentialWithUser:password:](./aspasswordcredential/credentialwithuser_password_.md)
  Creates a password credential instance with a given user name and password.
### Accessing the username and password
- [var user: String](./aspasswordcredential/user.md)
  The user for a password credential object.
- [var password: String](./aspasswordcredential/password.md)
  The password for a password credential object.
### Initializers
- [init?(coder: NSCoder)](./aspasswordcredential/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [ASAuthorizationCredential](./asauthorizationcredential.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Passwords
- [Password AutoFill](../Security/password-autofill.md)
  Streamline your app’s login and onboarding procedures.
- [class ASAuthorizationPasswordProvider](./asauthorizationpasswordprovider.md)
  A mechanism for generating requests to perform keychain credential sharing.
- [Password use in web browsers](./password-use-in-web-browsers.md)
  Register and authenticate website users by using passwords.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasswordcredential)*