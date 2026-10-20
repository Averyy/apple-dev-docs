# tokenEndpointURL

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The token endpoint URL for login requests.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var tokenEndpointURL: URL { get set }
```

```objc
@property (nonatomic, copy) NSURL * tokenEndpointURL;
```

## Mentions

- [Interpreting Platform Single Sign-on authorization scopes](../interpreting-platform-single-sign-on-authorization-scopes.md)

## See Also

### Obtaining the required configuration
- [var audience: String](./audience.md)
  The audience for validation and requests.
- [var clientID: String](./clientid.md)
  The identifier for the client at the identity provider.
- [var jwksEndpointURL: URL](./jwksendpointurl.md)
  The JSON Web Key Set endpoint URL for keys.
- [var issuer: String](./issuer.md)
  The issuer of the identity token that the identity provider returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/tokenendpointurl)*