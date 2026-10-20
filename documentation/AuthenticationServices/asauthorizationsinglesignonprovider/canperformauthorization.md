# canPerformAuthorization

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the provider is capable of performing authorization within a given configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var canPerformAuthorization: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL canPerformAuthorization;
```

## See Also

### Creating Authorization Requests
- [func createRequest() -> ASAuthorizationSingleSignOnRequest](./createrequest%28%29.md)
  Creates a single sign-on (SSO) authorization request.
- [class ASAuthorizationSingleSignOnRequest](../asauthorizationsinglesignonrequest.md)
  An OpenID authorization request that provides single sign-on (SSO) functionality.
- [class ASAuthorizationOpenIDRequest](../asauthorizationopenidrequest.md)
  An OpenID authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsinglesignonprovider/canperformauthorization)*