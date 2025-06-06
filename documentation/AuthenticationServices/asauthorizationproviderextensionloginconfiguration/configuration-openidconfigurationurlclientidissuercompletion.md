# configuration(openIDConfigurationURL:clientID:issuer:completion:)

**Framework**: Authentication Services  
**Kind**: method

Creates a login configuration using the OpenID configuration.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class func configuration(openIDConfigurationURL: URL, clientID: String, issuer: String?) async throws -> ASAuthorizationProviderExtensionLoginConfiguration
```

## Parameters

- `openIDConfigurationURL`: The base URL to retrieve the   file.
- `clientID`: The   for the Apple platform SSO login at the identity provider.
- `issuer`: The   for the requests that validate responses.
- `completion`: The completion block the system calls upon completion or error.

## See Also

- [init(clientID: String, issuer: String, tokenEndpointURL: URL, jwksEndpointURL: URL, audience: String?)](asauthorizationproviderextensionloginconfiguration/init(clientid:issuer:tokenendpointurl:jwksendpointurl:audience:).md)
  Creates a configuration with the required values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/configuration(openidconfigurationurl:clientid:issuer:completion:))*