# nonceResponseKeypath

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The keypath in the response that contains the one-time use value.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var nonceResponseKeypath: String { get set }
```

```objc
@property (nonatomic, copy) NSString * nonceResponseKeypath;
```

## Mentions

- [Obtaining a server nonce](../obtaining-a-server-nonce.md)

## Discussion

## See Also

### Configuring the server nonce
- [var customNonceRequestValues: [URLQueryItem]](./customnoncerequestvalues.md)
  Custom values to add to the server nonce POST request body.
- [var nonceEndpointURL: URL](./nonceendpointurl.md)
  The URL to retrieve a one-time use value from the server.
- [var serverNonceClaimName: String](./servernonceclaimname.md)
  The name of the claim to include in authentication requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/nonceresponsekeypath)*