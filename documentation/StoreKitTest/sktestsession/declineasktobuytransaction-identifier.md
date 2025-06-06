# declineAskToBuyTransaction(identifier:)

**Framework**: StoreKit Test  
**Kind**: method

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

## Parameters

- `identifier`: The transaction   of an Ask to Buy transaction.

## See Also

- [var askToBuyEnabled: Bool](sktestsession/asktobuyenabled.md)
  A Boolean value that determines whether the testing environment simulates an Ask to Buy scenario.
- [func approveAskToBuyTransaction(identifier: Int) throws](sktestsession/approveasktobuytransaction(identifier:).md)
  Resolves an Ask to Buy test scenario by approving the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/declineasktobuytransaction(identifier:))*