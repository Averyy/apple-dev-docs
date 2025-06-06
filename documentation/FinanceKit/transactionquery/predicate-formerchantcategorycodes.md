# predicate(forMerchantCategoryCodes:)

**Framework**: FinanceKit  
**Kind**: method

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/transactionquery/predicate(formerchantcategorycodes:))*