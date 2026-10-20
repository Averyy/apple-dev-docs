# predicate(forMerchantCategoryCodes:)

**Framework**: FinanceKit  
**Kind**: method  
**Role**: Type Method

A predicate that returns transactions that match any of the provided merchant category codes.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
static func predicate(forMerchantCategoryCodes merchantCategoryCodes: [MerchantCategoryCode]) -> Predicate<Transaction>
```

## Parameters

- `merchantCategoryCodes`: Merchant category codes to match against.

## See Also

### Type Methods
- [static func predicate(forStatuses: [TransactionStatus]) -> Predicate<Transaction>](./predicate%28forstatuses%29.md)
  Returns a predicate that matches any of the provided transaction statuses.
- [static func predicate(forTransactionTypes: [TransactionType]) -> Predicate<Transaction>](./predicate%28fortransactiontypes%29.md)
  Returns a predicate that matches any of the provided transaction types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/transactionquery/predicate(formerchantcategorycodes:))*