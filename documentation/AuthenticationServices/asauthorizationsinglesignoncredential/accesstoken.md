# accessToken

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

An access token used to get an identity token.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var accessToken: Data? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSData * accessToken;
```

## See Also

### Identifying a User
- [var identityToken: Data?](./identitytoken.md)
  A JSON Web Token (JWT) that securely communicates information about the user to your app.
- [var state: String?](./state.md)
  An arbitrary string that your app provided to the request that generated this credential.
- [var authorizedScopes: [ASAuthorization.Scope]](./authorizedscopes.md)
  The contact information the user authorized your app to access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsinglesignoncredential/accesstoken)*