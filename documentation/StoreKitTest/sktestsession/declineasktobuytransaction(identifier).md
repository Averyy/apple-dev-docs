# declineAskToBuyTransaction(identifier:)

**Framework**: StoreKit Test  
**Kind**: method  
**Role**: Instance Method

Resolves an Ask to Buy test scenario by declining the transaction.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func declineAskToBuyTransaction(identifier: Int) throws
```

```objc
- (BOOL) declineAskToBuyTransactionWithIdentifier:(NSUInteger) identifier error:(NSError **) error;
```

## Parameters

- `identifier`: The transaction [`identifier`](../sktesttransaction/identifier.md) of an Ask to Buy transaction.

## See Also

### Testing Ask To Buy transactions
- [var askToBuyEnabled: Bool](./asktobuyenabled.md)
  A Boolean value that determines whether the testing environment simulates an Ask to Buy scenario.
- [func approveAskToBuyTransaction(identifier: Int) throws](./approveasktobuytransaction%28identifier%29.md)
  Resolves an Ask to Buy test scenario by approving the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/declineasktobuytransaction(identifier:))*