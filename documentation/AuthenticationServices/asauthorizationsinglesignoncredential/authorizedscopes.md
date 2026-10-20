# authorizedScopes

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The contact information the user authorized your app to access.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var authorizedScopes: [ASAuthorization.Scope] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<NSString *> * authorizedScopes;
```

## See Also

### Identifying a User
- [var identityToken: Data?](./identitytoken.md)
  A JSON Web Token (JWT) that securely communicates information about the user to your app.
- [var accessToken: Data?](./accesstoken.md)
  An access token used to get an identity token.
- [var state: String?](./state.md)
  An arbitrary string that your app provided to the request that generated this credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsinglesignoncredential/authorizedscopes)*