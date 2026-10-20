# customNonceRequestValues

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

Custom values to add to the server nonce POST request body.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var customNonceRequestValues: [URLQueryItem] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSURLQueryItem *> * customNonceRequestValues;
```

## Mentions

- [Obtaining a server nonce](../obtaining-a-server-nonce.md)

## See Also

### Configuring the server nonce
- [var nonceEndpointURL: URL](./nonceendpointurl.md)
  The URL to retrieve a one-time use value from the server.
- [var nonceResponseKeypath: String](./nonceresponsekeypath.md)
  The keypath in the response that contains the one-time use value.
- [var serverNonceClaimName: String](./servernonceclaimname.md)
  The name of the claim to include in authentication requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/customnoncerequestvalues)*