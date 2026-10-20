# clientID

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The identifier for the client at the identity provider.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var clientID: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * clientID;
```

## Mentions

- [Processing the JSON Web Encryption (JWE) login response](../processing-the-json-web-encryption-jwe-login-response.md)
- [Creating a refresh request](../creating-a-refresh-request.md)
- [Creating and validating a login request](../creating-and-validating-a-login-request.md)
- [Supporting key requests and key exchange requests](../supporting-key-requests-and-key-exchange-requests.md)

## See Also

### Obtaining the required configuration
- [var audience: String](./audience.md)
  The audience for validation and requests.
- [var jwksEndpointURL: URL](./jwksendpointurl.md)
  The JSON Web Key Set endpoint URL for keys.
- [var tokenEndpointURL: URL](./tokenendpointurl.md)
  The token endpoint URL for login requests.
- [var issuer: String](./issuer.md)
  The issuer of the identity token that the identity provider returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/clientid)*