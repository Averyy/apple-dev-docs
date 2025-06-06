# init(clientID:issuer:tokenEndpointURL:jwksEndpointURL:audience:)

**Framework**: Authentication Services  
**Kind**: init

Creates a configuration with the required values.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(clientID: String, issuer: String, tokenEndpointURL: URL, jwksEndpointURL: URL, audience: String?)
```

## Parameters

- `clientID`: The OAuth   for the login.
- `issuer`: The OAuth   for validating the token.
- `tokenEndpointURL`: The token endpoint for login.
- `jwksEndpointURL`: The URL that retrieves the JSON Web Key Set (JWKS).
- `audience`: The OAuth   for embedded assertions.

## See Also

- [class func configuration(openIDConfigurationURL: URL, clientID: String, issuer: String?, completion: (ASAuthorizationProviderExtensionLoginConfiguration?, (any Error)?) -> Void)](asauthorizationproviderextensionloginconfiguration/configuration(openidconfigurationurl:clientid:issuer:completion:).md)
  Creates a login configuration using the OpenID configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/init(clientid:issuer:tokenendpointurl:jwksendpointurl:audience:))*