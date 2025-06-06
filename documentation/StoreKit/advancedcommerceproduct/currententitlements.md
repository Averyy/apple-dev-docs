# currentEntitlements

**Framework**: StoreKit  
**Kind**: property

The transactions that entitle the customer to Advanced Commerce Items purchased using the generic product ID.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
var currentEntitlements: Transaction.Transactions { get }
```

## See Also

- [var allTransactions: Transaction.Transactions](advancedcommerceproduct/alltransactions.md)
  All transactions associated with the generic product ID.
- [var latestTransaction: VerificationResult<Transaction>?](advancedcommerceproduct/latesttransaction.md)
  The most recent transaction associated with the generic product ID, if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/advancedcommerceproduct/currententitlements)*