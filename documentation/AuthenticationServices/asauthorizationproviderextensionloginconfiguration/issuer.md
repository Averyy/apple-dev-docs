# issuer

**Framework**: Authentication Services  
**Kind**: property

The issuer of the identity token that the identity provider returns.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var issuer: String { get }
```

## Mentions

- [Processing the JSON Web Encryption (JWE) login response](processing-the-json-web-encryption-jwe-login-response.md)

## See Also

- [var audience: String](asauthorizationproviderextensionloginconfiguration/audience.md)
  The audience for validation and requests.
- [var clientID: String](asauthorizationproviderextensionloginconfiguration/clientid.md)
  The identifier for the client at the identity provider.
- [var jwksEndpointURL: URL](asauthorizationproviderextensionloginconfiguration/jwksendpointurl.md)
  The JSON Web Key Set endpoint URL for keys.
- [var tokenEndpointURL: URL](asauthorizationproviderextensionloginconfiguration/tokenendpointurl.md)
  The token endpoint URL for login requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/issuer)*