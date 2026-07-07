# predicate(forStatuses:)

**Framework**: FinanceKit  
**Kind**: method

Returns a predicate that matches any of the provided transaction statuses.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
static func predicate(forStatuses statuses: [TransactionStatus]) -> Predicate<Transaction>
```

## Parameters

- `statuses`: Transaction statuses to match against.

## See Also

- [static func predicate(forMerchantCategoryCodes: [MerchantCategoryCode]) -> Predicate<Transaction>](transactionquery/predicate(formerchantcategorycodes:).md)
  A predicate that returns transactions that match any of the provided merchant category codes.
- [static func predicate(forTransactionTypes: [TransactionType]) -> Predicate<Transaction>](transactionquery/predicate(fortransactiontypes:).md)
  Returns a predicate that matches any of the provided transaction types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/transactionquery/predicate(forstatuses:))*