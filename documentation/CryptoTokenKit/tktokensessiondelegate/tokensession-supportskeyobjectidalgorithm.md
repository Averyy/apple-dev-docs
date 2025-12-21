# tokenSession(_:supports:keyObjectID:algorithm:)

**Framework**: CryptoTokenKit  
**Kind**: method

Asks the delegate whether the token session supports a given operation using the specified key and algorithm.

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
optional func tokenSession(_ session: TKTokenSession, supports operation: TKTokenOperation, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the operation is supported; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `session`: The token session.
- `operation`: The operation to perform. For possible values, see  .
- `keyObjectID`: The identifier of the private key object.
- `algorithm`: The algorithm to be used by the operation.

## See Also

- [enum TKTokenOperation](tktokenoperation.md)
  Operations that can be performed with a token’s keys and certificates.
- [typealias ObjectID](tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.
- [class TKTokenKeyAlgorithm](tktokenkeyalgorithm.md)
  Cryptographic algorithms used by token keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/tokensession(_:supports:keyobjectid:algorithm:))*