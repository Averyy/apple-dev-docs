# ASAuthorization.OpenIDOperation

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

The kinds of operations that you can perform with OpenID authentication.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct OpenIDOperation
```

```c
typedef NSString * ASAuthorizationOpenIDOperation;
```

#### Discussion

Use one of these values as the [`requestedOperation`](../asauthorizationopenidrequest/requestedoperation.md) property in an OpenID request that you make with an instance of either [`ASAuthorizationAppleIDRequest`](../asauthorizationappleidrequest.md) or [`ASAuthorizationSingleSignOnRequest`](../asauthorizationsinglesignonrequest.md).

## Topics

### Operation Types
- [static let operationLogin: ASAuthorization.OpenIDOperation](./openidoperation/operationlogin.md)
  An operation used to authenticate a user.
- [static let operationRefresh: ASAuthorization.OpenIDOperation](./openidoperation/operationrefresh.md)
  An operation that refreshes the logged-in user’s credentials.
- [static let operationLogout: ASAuthorization.OpenIDOperation](./openidoperation/operationlogout.md)
  An operation that ends an authenticated session.
- [static let operationImplicit: ASAuthorization.OpenIDOperation](./openidoperation/operationimplicit.md)
  An operation that depends on the particular kind of credential provider.
### Creating an Operation
- [init(String)](./openidoperation/init%28_%29.md)
  Creates an operation from the given string.
- [init(rawValue: String)](./openidoperation/init%28rawvalue%29.md)
  Creates an operation from the given string.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Setting the Operation
- [var requestedOperation: ASAuthorization.OpenIDOperation](../asauthorizationopenidrequest/requestedoperation.md)
  The OpenID authentication operation you want this request to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorization/openidoperation)*