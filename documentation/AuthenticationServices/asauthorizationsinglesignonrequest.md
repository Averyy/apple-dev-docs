# ASAuthorizationSingleSignOnRequest

**Framework**: Authentication Services  
**Kind**: class

An OpenID authorization request that provides single sign-on (SSO) functionality.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class ASAuthorizationSingleSignOnRequest
```

## Topics

### Setting Options
- [var isUserInterfaceEnabled: Bool](asauthorizationsinglesignonrequest/isuserinterfaceenabled.md)
- [var authorizationOptions: [URLQueryItem]](asauthorizationsinglesignonrequest/authorizationoptions.md)
  Options that control the authorization process.

## Relationships

### Inherits From
- [ASAuthorizationOpenIDRequest](asauthorizationopenidrequest.md)
### Conforms To
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

- [var canPerformAuthorization: Bool](asauthorizationsinglesignonprovider/canperformauthorization.md)
  A Boolean value that indicates if the provider is capable of performing authorization within a given configuration.
- [func createRequest() -> ASAuthorizationSingleSignOnRequest](asauthorizationsinglesignonprovider/createrequest.md)
  Creates a single sign-on (SSO) authorization request.
- [class ASAuthorizationOpenIDRequest](asauthorizationopenidrequest.md)
  An OpenID authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsinglesignonrequest)*