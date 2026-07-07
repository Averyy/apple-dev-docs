# latestTransaction

**Framework**: StoreKit  
**Kind**: property

The most recent transaction associated with the generic product ID, if it exists.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
var latestTransaction: VerificationResult<Transaction>? { get async }
```

#### Discussion

This value is `nil` if the customer hasn’t made any purchases associated with the generic product ID.

## See Also

- [var allTransactions: Transaction.Transactions](advancedcommerceproduct/alltransactions.md)
  All transactions associated with the generic product ID.
- [var currentEntitlements: Transaction.Transactions](advancedcommerceproduct/currententitlements.md)
  The transactions that entitle the customer to Advanced Commerce Items purchased using the generic product ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/advancedcommerceproduct/latesttransaction)*