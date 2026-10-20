# TKTokenOperation

**Framework**: CryptoTokenKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum TKTokenOperation : NSInteger;
```

## Topics

### Constants
- [TKTokenOperation.none](./tktokenoperation/none.md)
- [TKTokenOperation.readData](./tktokenoperation/readdata.md)
- [TKTokenOperation.signData](./tktokenoperation/signdata.md)
- [TKTokenOperation.decryptData](./tktokenoperation/decryptdata.md)
- [TKTokenOperation.performKeyExchange](./tktokenoperation/performkeyexchange.md)
### Initializers
- [init?(rawValue: Int)](./tktokenoperation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Determining Support for Operations
- [func tokenSession(TKTokenSession, supports: TKTokenOperation, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) -> Bool](./tktokensessiondelegate/tokensession%28_,supports,keyobjectid,algorithm%29.md)
  Asks the delegate whether the token session supports a given operation using the specified key and algorithm.
- [typealias ObjectID](./tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.
- [class TKTokenKeyAlgorithm](./tktokenkeyalgorithm.md)
  Cryptographic algorithms used by token keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperation)*