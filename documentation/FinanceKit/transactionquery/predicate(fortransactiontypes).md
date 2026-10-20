# predicate(forTransactionTypes:)

**Framework**: FinanceKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate that matches any of the provided transaction types.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
static func predicate(forTransactionTypes transactionTypes: [TransactionType]) -> Predicate<Transaction>
```

## Parameters

- `transactionTypes`: Transaction types to match against.

## See Also

### Type Methods
- [static func predicate(forMerchantCategoryCodes: [MerchantCategoryCode]) -> Predicate<Transaction>](./predicate%28formerchantcategorycodes%29.md)
  A predicate that returns transactions that match any of the provided merchant category codes.
- [static func predicate(forStatuses: [TransactionStatus]) -> Predicate<Transaction>](./predicate%28forstatuses%29.md)
  Returns a predicate that matches any of the provided transaction statuses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/transactionquery/predicate(fortransactiontypes:))*