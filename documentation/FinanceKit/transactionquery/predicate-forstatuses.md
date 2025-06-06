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


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/transactionquery/predicate(forstatuses:))*