# deleteTransaction(identifier:)

**Framework**: StoreKit Test  
**Kind**: method

Deletes a specific transaction from the test environment.

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
func deleteTransaction(identifier: Int) throws
```

#### Discussion

When you delete a transaction, the test environment also removes the existing transaction from the receipt. Some transactions don’t appear in the receipt, including finished consumable purchases, failed purchases, Ask To Buy transactions pending approval, and restored purchases. Deleting a transaction deletes its child transactions, for example:

- Deleting an original subscription transaction deletes all related renewal transactions.
- Deleting a transaction deletes any associated restored transactions.

## Parameters

- `identifier`: The transaction identifier.

## See Also

- [func allTransactions() -> [SKTestTransaction]](sktestsession/alltransactions.md)
  Gets a list of all transactions in the test environment.
- [func clearTransactions()](sktestsession/cleartransactions.md)
  Removes all transactions from the test environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/deletetransaction(identifier:))*