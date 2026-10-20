# ASAuthorization.Scope

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

The kinds of contact information that can be requested from the user.

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
struct Scope
```

```c
typedef NSString * ASAuthorizationScope;
```

#### Discussion

Use one or more of these values in the [`requestedScopes`](../asauthorizationopenidrequest/requestedscopes.md) array that you configure in an instance of either [`ASAuthorizationAppleIDRequest`](../asauthorizationappleidrequest.md) or [`ASAuthorizationSingleSignOnRequest`](../asauthorizationsinglesignonrequest.md) to request certain contact information from the user.

Inspect the [`authorizedScopes`](../asauthorizationappleidcredential/authorizedscopes.md) array of an [`ASAuthorizationAppleIDCredential`](../asauthorizationappleidcredential.md) instance, or the (similarly named) [`authorizedScopes`](../asauthorizationsinglesignoncredential/authorizedscopes.md) array of an [`ASAuthorizationSingleSignOnCredential`](../asauthorizationsinglesignoncredential.md) instance, to see what scopes the user actually authorized. This might differ from the scopes you requested.

## Topics

### Scopes
- [static let email: ASAuthorization.Scope](./scope/email.md)
  A scope that includes the user’s email address.
- [static let fullName: ASAuthorization.Scope](./scope/fullname.md)
  A scope that includes the user’s full name.
### Creating a Scope
- [init(String)](./scope/init%28_%29.md)
  Creates a scope from the given string.
- [init(rawValue: String)](./scope/init%28rawvalue%29.md)
  Creates a scope from the given string.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Setting the Scope
- [var requestedScopes: [ASAuthorization.Scope]?](../asauthorizationopenidrequest/requestedscopes.md)
  The contact information to be requested from the user during authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorization/scope)*