# clientID

**Framework**: Authentication Services  
**Kind**: property

The identifier for the client at the identity provider.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var clientID: String { get }
```

## Mentions

- [Processing the JSON Web Encryption (JWE) login response](processing-the-json-web-encryption-jwe-login-response.md)
- [Creating a refresh request](creating-a-refresh-request.md)
- [Creating and validating a login request](creating-and-validating-a-login-request.md)
- [Supporting key requests and key exchange requests](supporting-key-requests-and-key-exchange-requests.md)

## See Also

- [var audience: String](asauthorizationproviderextensionloginconfiguration/audience.md)
  The audience for validation and requests.
- [var jwksEndpointURL: URL](asauthorizationproviderextensionloginconfiguration/jwksendpointurl.md)
  The JSON Web Key Set endpoint URL for keys.
- [var tokenEndpointURL: URL](asauthorizationproviderextensionloginconfiguration/tokenendpointurl.md)
  The token endpoint URL for login requests.
- [var issuer: String](asauthorizationproviderextensionloginconfiguration/issuer.md)
  The issuer of the identity token that the identity provider returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/clientid)*