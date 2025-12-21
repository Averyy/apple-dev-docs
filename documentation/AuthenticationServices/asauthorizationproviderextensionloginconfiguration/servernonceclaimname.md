# serverNonceClaimName

**Framework**: Authentication Services  
**Kind**: property

The name of the claim to include in authentication requests.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var serverNonceClaimName: String { get set }
```

## Mentions

- [Creating an embedded assertion](creating-an-embedded-assertion.md)
- [Supporting key requests and key exchange requests](supporting-key-requests-and-key-exchange-requests.md)
- [Creating a refresh request](creating-a-refresh-request.md)
- [Creating an encrypted embedded assertion](creating-an-encrypted-embedded-assertion.md)
- [Creating and validating a login request](creating-and-validating-a-login-request.md)

#### Discussion

The default value is `request_nonce`.

## See Also

- [var customNonceRequestValues: [URLQueryItem]](asauthorizationproviderextensionloginconfiguration/customnoncerequestvalues.md)
  Custom values to add to the server nonce POST request body.
- [var nonceEndpointURL: URL](asauthorizationproviderextensionloginconfiguration/nonceendpointurl.md)
  The URL to retrieve a one-time use value from the server.
- [var nonceResponseKeypath: String](asauthorizationproviderextensionloginconfiguration/nonceresponsekeypath.md)
  The keypath in the response that contains the one-time use value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/servernonceclaimname)*