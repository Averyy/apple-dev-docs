# nonceEndpointURL

**Framework**: Authentication Services  
**Kind**: property

The URL to retrieve a one-time use value from the server.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var nonceEndpointURL: URL { get set }
```

## Mentions

- [Obtaining a server nonce](obtaining-a-server-nonce.md)

#### Discussion

The value of this property defaults to [`tokenEndpointURL`](asauthorizationproviderextensionloginconfiguration/tokenendpointurl.md).

## See Also

- [var customNonceRequestValues: [URLQueryItem]](asauthorizationproviderextensionloginconfiguration/customnoncerequestvalues.md)
  Custom values to add to the server nonce POST request body.
- [var nonceResponseKeypath: String](asauthorizationproviderextensionloginconfiguration/nonceresponsekeypath.md)
  The keypath in the response that contains the one-time use value.
- [var serverNonceClaimName: String](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md)
  The name of the claim to include in authentication requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/nonceendpointurl)*