# audience

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The audience for validation and requests.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var audience: String { get set }
```

```objc
@property (nonatomic, copy) NSString * audience;
```

## Mentions

- [Supporting key requests and key exchange requests](../supporting-key-requests-and-key-exchange-requests.md)
- [Creating an embedded assertion](../creating-an-embedded-assertion.md)
- [Creating an encrypted embedded assertion](../creating-an-encrypted-embedded-assertion.md)

## See Also

### Obtaining the required configuration
- [var clientID: String](./clientid.md)
  The identifier for the client at the identity provider.
- [var jwksEndpointURL: URL](./jwksendpointurl.md)
  The JSON Web Key Set endpoint URL for keys.
- [var tokenEndpointURL: URL](./tokenendpointurl.md)
  The token endpoint URL for login requests.
- [var issuer: String](./issuer.md)
  The issuer of the identity token that the identity provider returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/audience)*