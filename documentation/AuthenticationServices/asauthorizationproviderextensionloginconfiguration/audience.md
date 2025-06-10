# audience

**Framework**: Authentication Services  
**Kind**: property

The audience for validation and requests.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var audience: String { get set }
```

## Mentions

- [Supporting key requests and key exchange requests](supporting-key-requests-and-key-exchange-requests.md)
- [Creating an embedded assertion](creating-an-embedded-assertion.md)
- [Creating an encrypted embedded assertion](creating-an-encrypted-embedded-assertion.md)

## See Also

- [var clientID: String](asauthorizationproviderextensionloginconfiguration/clientid.md)
  The identifier for the client at the identity provider.
- [var jwksEndpointURL: URL](asauthorizationproviderextensionloginconfiguration/jwksendpointurl.md)
  The JSON Web Key Set endpoint URL for keys.
- [var tokenEndpointURL: URL](asauthorizationproviderextensionloginconfiguration/tokenendpointurl.md)
  The token endpoint URL for login requests.
- [var issuer: String](asauthorizationproviderextensionloginconfiguration/issuer.md)
  The issuer of the identity token that the identity provider returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/audience)*