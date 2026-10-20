# ASAuthorizationSingleSignOnRequest

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASAuthorizationSingleSignOnRequest : ASAuthorizationOpenIDRequest
```

## Topics

### Setting Options
- [var isUserInterfaceEnabled: Bool](./asauthorizationsinglesignonrequest/isuserinterfaceenabled.md)
- [var authorizationOptions: [URLQueryItem]](./asauthorizationsinglesignonrequest/authorizationoptions.md)
  Options that control the authorization process.

## Relationships

### Inherits From
- [ASAuthorizationOpenIDRequest](./asauthorizationopenidrequest.md)
### Conforms To
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

### Creating Authorization Requests
- [var canPerformAuthorization: Bool](./asauthorizationsinglesignonprovider/canperformauthorization.md)
  A Boolean value that indicates if the provider is capable of performing authorization within a given configuration.
- [func createRequest() -> ASAuthorizationSingleSignOnRequest](./asauthorizationsinglesignonprovider/createrequest%28%29.md)
  Creates a single sign-on (SSO) authorization request.
- [class ASAuthorizationOpenIDRequest](./asauthorizationopenidrequest.md)
  An OpenID authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsinglesignonrequest)*