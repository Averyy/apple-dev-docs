# jwksEndpointURL

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The JSON Web Key Set endpoint URL for keys.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var jwksEndpointURL: URL { get set }
```

```objc
@property (nonatomic, copy) NSURL * jwksEndpointURL;
```

## Mentions

- [Processing the JSON Web Encryption (JWE) login response](../processing-the-json-web-encryption-jwe-login-response.md)

## See Also

### Obtaining the required configuration
- [var audience: String](./audience.md)
  The audience for validation and requests.
- [var clientID: String](./clientid.md)
  The identifier for the client at the identity provider.
- [var tokenEndpointURL: URL](./tokenendpointurl.md)
  The token endpoint URL for login requests.
- [var issuer: String](./issuer.md)
  The issuer of the identity token that the identity provider returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/jwksendpointurl)*