# TKTokenKeyExchangeParameters

**Framework**: CryptoTokenKit  
**Kind**: class

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

## Topics

### Accessing Parameters
- [var requestedSize: Int](tktokenkeyexchangeparameters/requestedsize.md)
  Returns the requested output size, in bytes, of key exchange result.
- [var sharedInfo: Data?](tktokenkeyexchangeparameters/sharedinfo.md)
  Returns shared information typically used during the key derivation (KDF) step of a key exchange algorithm.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func tokenSession(TKTokenSession, sign: Data, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) throws -> Data](tktokensessiondelegate/tokensession(_:sign:keyobjectid:algorithm:).md)
  Tells the delegate to sign a data object using the specified key and algorithm.
- [func tokenSession(TKTokenSession, decrypt: Data, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) throws -> Data](tktokensessiondelegate/tokensession(_:decrypt:keyobjectid:algorithm:).md)
  Tells the delegate to decrypt a data object using the specified key and algorithm.
- [func tokenSession(TKTokenSession, performKeyExchange: Data, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm, parameters: TKTokenKeyExchangeParameters) throws -> Data](tktokensessiondelegate/tokensession(_:performkeyexchange:keyobjectid:algorithm:parameters:).md)
  Tells the delegate to perform a key exchange using the specified key and algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeyexchangeparameters)*