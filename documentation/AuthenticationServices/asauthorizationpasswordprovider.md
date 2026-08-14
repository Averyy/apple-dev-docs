# ASAuthorizationPasswordProvider

**Framework**: Authentication Services  
**Kind**: class

A mechanism for generating requests to perform keychain credential sharing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class ASAuthorizationPasswordProvider
```

## Topics

### Creating Requests
- [func createRequest() -> ASAuthorizationPasswordRequest](asauthorizationpasswordprovider/createrequest.md)
  Creates a new password authorization request.
- [class ASAuthorizationPasswordRequest](asauthorizationpasswordrequest.md)
  An authorization request that uses credentials stored in the keychain.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [ASAuthorizationProvider](asauthorizationprovider.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Password AutoFill](../security/password-autofill.md)
  Streamline your app’s login and onboarding procedures.
- [class ASPasswordCredential](aspasswordcredential.md)
  A password credential.
- [Password use in web browsers](password-use-in-web-browsers.md)
  Register and authenticate website users by using passwords.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpasswordprovider)*