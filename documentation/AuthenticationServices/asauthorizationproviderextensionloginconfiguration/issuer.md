# issuer

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The issuer of the identity token that the identity provider returns.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var issuer: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * issuer;
```

## Mentions

- [Processing the JSON Web Encryption (JWE) login response](../processing-the-json-web-encryption-jwe-login-response.md)

## See Also

### Obtaining the required configuration
- [var audience: String](./audience.md)
  The audience for validation and requests.
- [var clientID: String](./clientid.md)
  The identifier for the client at the identity provider.
- [var jwksEndpointURL: URL](./jwksendpointurl.md)
  The JSON Web Key Set endpoint URL for keys.
- [var tokenEndpointURL: URL](./tokenendpointurl.md)
  The token endpoint URL for login requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/issuer)*