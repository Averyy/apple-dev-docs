# customNonceRequestValues

**Framework**: Authentication Services  
**Kind**: property

Custom values to add to the server nonce POST request body.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var customNonceRequestValues: [URLQueryItem] { get set }
```

## Mentions

- [Obtaining a server nonce](obtaining-a-server-nonce.md)

## See Also

- [var nonceEndpointURL: URL](asauthorizationproviderextensionloginconfiguration/nonceendpointurl.md)
  The URL to retrieve a one-time use value from the server.
- [var nonceResponseKeypath: String](asauthorizationproviderextensionloginconfiguration/nonceresponsekeypath.md)
  The keypath in the response that contains the one-time use value.
- [var serverNonceClaimName: String](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md)
  The name of the claim to include in authentication requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/customnoncerequestvalues)*