# TKTokenOperation

**Framework**: CryptoTokenKit  
**Kind**: enum

Operations that can be performed with a token’s keys and certificates.

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
enum TKTokenOperation
```

## Topics

### Constants
- [TKTokenOperation.none](tktokenoperation/none.md)
- [TKTokenOperation.readData](tktokenoperation/readdata.md)
- [TKTokenOperation.signData](tktokenoperation/signdata.md)
- [TKTokenOperation.decryptData](tktokenoperation/decryptdata.md)
- [TKTokenOperation.performKeyExchange](tktokenoperation/performkeyexchange.md)
### Initializers
- [init?(rawValue: Int)](tktokenoperation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func tokenSession(TKTokenSession, supports: TKTokenOperation, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) -> Bool](tktokensessiondelegate/tokensession(_:supports:keyobjectid:algorithm:).md)
  Asks the delegate whether the token session supports a given operation using the specified key and algorithm.
- [typealias ObjectID](tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.
- [class TKTokenKeyAlgorithm](tktokenkeyalgorithm.md)
  Cryptographic algorithms used by token keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperation)*