# configuration(openIDConfigurationURL:clientID:issuer:completion:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Type Method

Creates a login configuration using the OpenID configuration.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class func configuration(openIDConfigurationURL: URL, clientID: String, issuer: String?, completion: @escaping @Sendable (ASAuthorizationProviderExtensionLoginConfiguration?, (any Error)?) -> Void)
```

```swift
class func configuration(openIDConfigurationURL: URL, clientID: String, issuer: String?) async throws -> ASAuthorizationProviderExtensionLoginConfiguration
```

```objc
+ (void) configurationWithOpenIDConfigurationURL:(NSURL *) openIDConfigurationURL clientID:(NSString *) clientID issuer:(NSString *) issuer completion:(void (^)(ASAuthorizationProviderExtensionLoginConfiguration *loginConfiguration, NSError *error)) completion;
```

## Parameters

- `openIDConfigurationURL`: The base URL to retrieve the `/.well-known/openid-configuration` file.
- `clientID`: The `client_id` for the Apple platform SSO login at the identity provider.
- `issuer`: The `issuer` for the requests that validate responses.
- `completion`: The completion block the system calls upon completion or error.

## See Also

### Creating the configuration
- [init(clientID: String, issuer: String, tokenEndpointURL: URL, jwksEndpointURL: URL, audience: String?)](./init%28clientid,issuer,tokenendpointurl,jwksendpointurl,audience%29.md)
  Creates a configuration with the required values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/configuration(openidconfigurationurl:clientid:issuer:completion:))*