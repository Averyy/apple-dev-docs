# allTransactions()

**Framework**: StoreKit Test  
**Kind**: method

Gets a list of all transactions in the test environment.

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
func allTransactions() -> [SKTestTransaction]
```

#### Return Value

An array that contains all transactions.

#### Discussion

This array contains all transactions, including those that don’t appear in the receipt, such as:

- Failed transactions
- Pending Ask to Buy transactions
- Purchases of consumable products

Use this list to work with Ask to Buy, to refund a specific transaction, or delete a transaction from the history, so you can repeat the test.

## See Also

- [func deleteTransaction(identifier: Int) throws](sktestsession/deletetransaction(identifier:).md)
  Deletes a specific transaction from the test environment.
- [func clearTransactions()](sktestsession/cleartransactions.md)
  Removes all transactions from the test environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/alltransactions())*