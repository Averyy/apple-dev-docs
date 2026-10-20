# allTransactions()

**Framework**: StoreKit Test  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSArray<SKTestTransaction *> *) allTransactions;
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

### Managing transactions in the test environment
- [func deleteTransaction(identifier: Int) throws](./deletetransaction%28identifier%29.md)
  Deletes a specific transaction from the test environment.
- [func clearTransactions()](./cleartransactions%28%29.md)
  Removes all transactions from the test environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/alltransactions())*