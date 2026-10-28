# tokenSession(_:decrypt:keyObjectID:algorithm:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to decrypt a data object using the specified key and algorithm.

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
optional func tokenSession(_ session: TKTokenSession, decrypt ciphertext: Data, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) throws -> Data
```

```objc
- (NSData *) tokenSession:(TKTokenSession *) session decryptData:(NSData *) ciphertext usingKey:(TKTokenObjectID) keyObjectID algorithm:(TKTokenKeyAlgorithm *) algorithm error:(NSError **) error;
```

## Return Value

The decrypted data, or `nil` if an error occurred.

## Parameters

- `session`: The token session.
- `ciphertext`: The data to decrypt.
- `keyObjectID`: The identifier of the public key object.
- `algorithm`: The algorithm to be used for decryption.

## See Also

### Performing Cryptographic Operations
- [func tokenSession(TKTokenSession, sign: Data, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) throws -> Data](./tokensession%28_,sign,keyobjectid,algorithm%29.md)
  Tells the delegate to sign a data object using the specified key and algorithm.
- [func tokenSession(TKTokenSession, performKeyExchange: Data, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm, parameters: TKTokenKeyExchangeParameters) throws -> Data](./tokensession%28_,performkeyexchange,keyobjectid,algorithm,parameters%29.md)
  Tells the delegate to perform a key exchange using the specified key and algorithm.
- [class TKTokenKeyExchangeParameters](../tktokenkeyexchangeparameters.md)
  Parameters used to perform specific key exchange operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/tokensession(_:decrypt:keyobjectid:algorithm:))*