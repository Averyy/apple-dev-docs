# tokenSession(_:performKeyExchange:keyObjectID:algorithm:parameters:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to perform a key exchange using the specified key and algorithm.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func tokenSession(_ session: TKTokenSession, performKeyExchange otherPartyPublicKeyData: Data, keyObjectID objectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm, parameters: TKTokenKeyExchangeParameters) throws -> Data
```

```objc
- (NSData *) tokenSession:(TKTokenSession *) session performKeyExchangeWithPublicKey:(NSData *) otherPartyPublicKeyData usingKey:(TKTokenObjectID) objectID algorithm:(TKTokenKeyAlgorithm *) algorithm parameters:(TKTokenKeyExchangeParameters *) parameters error:(NSError **) error;
```

## Return Value

The result of the key exchange, or `nil` if an error occurred.

## Parameters

- `session`: The token session.
- `otherPartyPublicKeyData`: The public key of the other party.
- `objectID`: The identifier of the private key object.
- `algorithm`: The algorithm to be used for key exchange.
- `parameters`: Additional parameters used by `algorithm` to perform the key exchange.

## See Also

### Performing Cryptographic Operations
- [func tokenSession(TKTokenSession, sign: Data, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) throws -> Data](./tokensession%28_,sign,keyobjectid,algorithm%29.md)
  Tells the delegate to sign a data object using the specified key and algorithm.
- [func tokenSession(TKTokenSession, decrypt: Data, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) throws -> Data](./tokensession%28_,decrypt,keyobjectid,algorithm%29.md)
  Tells the delegate to decrypt a data object using the specified key and algorithm.
- [class TKTokenKeyExchangeParameters](../tktokenkeyexchangeparameters.md)
  Parameters used to perform specific key exchange operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/tokensession(_:performkeyexchange:keyobjectid:algorithm:parameters:))*