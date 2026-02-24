# init(sortDescriptors:predicate:limit:offset:)

**Framework**: FinanceKit  
**Kind**: init

Creates a new transaction query with the provided sort descriptors, predicate, and limit on the number of records the query should return.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
init(sortDescriptors: [SortDescriptor<Transaction>] = [], predicate: Predicate<Transaction>? = nil, limit: Int? = nil, offset: Int? = nil)
```

## Parameters

- `sortDescriptors`: An array of [`Transaction`](transaction.md) sort descriptors.
- `predicate`: A [`Predicate`](https://developer.apple.com/documentation/Foundation/Predicate) to filter the `Transaction` records with.
- `limit`: An integer that indicates the maximum number of `Transaction` records to return.
- `offset`: An integer that indicates the number of records to offset the result by.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/transactionquery/init(sortdescriptors:predicate:limit:offset:))*