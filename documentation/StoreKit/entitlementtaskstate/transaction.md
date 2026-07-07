# transaction

**Framework**: StoreKit  
**Kind**: property

The transaction value if the task is successful.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var transaction: VerificationResult<Transaction>? { get }
```

#### Discussion

Use [`transaction`](entitlementtaskstate/transaction.md) as a convenience to access the transaction value in code that doesn’t depend on the reason a transaction isn’t available. The value is `nil` while the transaction is loading, if it fails to load for any reason, or if the customer isn’t entitled to the product.

## See Also

- [var value: Value?](entitlementtaskstate/value.md)
  The entitlement value if the task is successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/entitlementtaskstate/transaction)*