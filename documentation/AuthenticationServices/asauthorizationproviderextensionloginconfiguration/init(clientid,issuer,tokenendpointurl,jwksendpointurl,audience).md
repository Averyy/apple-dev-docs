# init(clientID:issuer:tokenEndpointURL:jwksEndpointURL:audience:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

Creates a configuration with the required values.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(clientID: String, issuer: String, tokenEndpointURL: URL, jwksEndpointURL: URL, audience: String?)
```

```objc
- (instancetype) initWithClientID:(NSString *) clientID issuer:(NSString *) issuer tokenEndpointURL:(NSURL *) tokenEndpointURL jwksEndpointURL:(NSURL *) jwksEndpointURL audience:(NSString *) audience;
```

## Parameters

- `clientID`: The OAuth `client_id` for the login.
- `issuer`: The OAuth `issuer` for validating the token.
- `tokenEndpointURL`: The token endpoint for login.
- `jwksEndpointURL`: The URL that retrieves the JSON Web Key Set (JWKS).
- `audience`: The OAuth `audence` for embedded assertions.

## See Also

### Creating the configuration
- [class func configuration(openIDConfigurationURL: URL, clientID: String, issuer: String?, completion: (ASAuthorizationProviderExtensionLoginConfiguration?, (any Error)?) -> Void)](./configuration%28openidconfigurationurl,clientid,issuer,completion%29.md)
  Creates a login configuration using the OpenID configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/init(clientid:issuer:tokenendpointurl:jwksendpointurl:audience:))*