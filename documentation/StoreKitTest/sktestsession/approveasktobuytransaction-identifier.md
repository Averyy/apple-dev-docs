# approveAskToBuyTransaction(identifier:)

**Framework**: StoreKit Test  
**Kind**: method

Resolves an Ask to Buy test scenario by approving the transaction.

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
func approveAskToBuyTransaction(identifier: Int) throws
```

## Parameters

- `identifier`: The transaction   of the Ask to Buy transaction.

## See Also

- [var askToBuyEnabled: Bool](sktestsession/asktobuyenabled.md)
  A Boolean value that determines whether the testing environment simulates an Ask to Buy scenario.
- [func declineAskToBuyTransaction(identifier: Int) throws](sktestsession/declineasktobuytransaction(identifier:).md)
  Resolves an Ask to Buy test scenario by declining the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/approveasktobuytransaction(identifier:))*