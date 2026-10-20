# TKTokenKeyExchangeParameters

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

Parameters used to perform specific key exchange operations.

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
class TKTokenKeyExchangeParameters
```

```objc
@interface TKTokenKeyExchangeParameters : NSObject
```

## Topics

### Accessing Parameters
- [var requestedSize: Int](./tktokenkeyexchangeparameters/requestedsize.md)
  Returns the requested output size, in bytes, of key exchange result.
- [var sharedInfo: Data?](./tktokenkeyexchangeparameters/sharedinfo.md)
  Returns shared information typically used during the key derivation (KDF) step of a key exchange algorithm.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Performing Cryptographic Operations
- [func tokenSession(TKTokenSession, sign: Data, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) throws -> Data](./tktokensessiondelegate/tokensession%28_,sign,keyobjectid,algorithm%29.md)
  Tells the delegate to sign a data object using the specified key and algorithm.
- [func tokenSession(TKTokenSession, decrypt: Data, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) throws -> Data](./tktokensessiondelegate/tokensession%28_,decrypt,keyobjectid,algorithm%29.md)
  Tells the delegate to decrypt a data object using the specified key and algorithm.
- [func tokenSession(TKTokenSession, performKeyExchange: Data, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm, parameters: TKTokenKeyExchangeParameters) throws -> Data](./tktokensessiondelegate/tokensession%28_,performkeyexchange,keyobjectid,algorithm,parameters%29.md)
  Tells the delegate to perform a key exchange using the specified key and algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeyexchangeparameters)*