# TKTokenSessionDelegate

**Framework**: CryptoTokenKit  
**Kind**: protocol

The interface that a session instance delegate implements to respond to token session authentication events.

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
protocol TKTokenSessionDelegate : NSObjectProtocol
```

## Topics

### Determining Support for Operations
- [func tokenSession(TKTokenSession, supports: TKTokenOperation, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) -> Bool](tktokensessiondelegate/tokensession(_:supports:keyobjectid:algorithm:).md)
  Asks the delegate whether the token session supports a given operation using the specified key and algorithm.
- [enum TKTokenOperation](tktokenoperation.md)
  Operations that can be performed with a token’s keys and certificates.
- [typealias ObjectID](tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.
- [class TKTokenKeyAlgorithm](tktokenkeyalgorithm.md)
  Cryptographic algorithms used by token keys.
### Authenticating
- [func tokenSession(TKTokenSession, beginAuthFor: TKTokenOperation, constraint: Any) throws -> TKTokenAuthOperation](tktokensessiondelegate/tokensession(_:beginauthfor:constraint:).md)
  Tells the delegate that authentication has begun for the specified operation and constraint.
- [typealias TKTokenOperationConstraint](tktokenoperationconstraint.md)
  A token’s authentication constraint for a specific operation.
- [class TKTokenAuthOperation](tktokenauthoperation.md)
  An authentication operation for a cryptographic token.
- [class TKTokenPasswordAuthOperation](tktokenpasswordauthoperation.md)
  A password-based authentication operation.
- [class TKTokenSmartCardPINAuthOperation](tktokensmartcardpinauthoperation.md)
  A Smart Card PIN authentication operation.
### Performing Cryptographic Operations
- [func tokenSession(TKTokenSession, sign: Data, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) throws -> Data](tktokensessiondelegate/tokensession(_:sign:keyobjectid:algorithm:).md)
  Tells the delegate to sign a data object using the specified key and algorithm.
- [func tokenSession(TKTokenSession, decrypt: Data, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) throws -> Data](tktokensessiondelegate/tokensession(_:decrypt:keyobjectid:algorithm:).md)
  Tells the delegate to decrypt a data object using the specified key and algorithm.
- [func tokenSession(TKTokenSession, performKeyExchange: Data, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm, parameters: TKTokenKeyExchangeParameters) throws -> Data](tktokensessiondelegate/tokensession(_:performkeyexchange:keyobjectid:algorithm:parameters:).md)
  Tells the delegate to perform a key exchange using the specified key and algorithm.
- [class TKTokenKeyExchangeParameters](tktokenkeyexchangeparameters.md)
  Parameters used to perform specific key exchange operations.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any TKTokenSessionDelegate)?](tktokensession/delegate.md)
  The token session delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate)*