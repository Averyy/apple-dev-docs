# nonceResponseKeypath

**Framework**: Authentication Services  
**Kind**: property

The keypath in the response that contains the one-time use value.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var nonceResponseKeypath: String { get set }
```

## Mentions

- [Obtaining a server nonce](obtaining-a-server-nonce.md)

#### Discussion

## See Also

- [var customNonceRequestValues: [URLQueryItem]](asauthorizationproviderextensionloginconfiguration/customnoncerequestvalues.md)
  Custom values to add to the server nonce POST request body.
- [var nonceEndpointURL: URL](asauthorizationproviderextensionloginconfiguration/nonceendpointurl.md)
  The URL to retrieve a one-time use value from the server.
- [var serverNonceClaimName: String](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md)
  The name of the claim to include in authentication requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/nonceresponsekeypath)*