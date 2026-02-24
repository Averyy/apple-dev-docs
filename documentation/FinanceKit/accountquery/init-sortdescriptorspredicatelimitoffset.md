# init(sortDescriptors:predicate:limit:offset:)

**Framework**: FinanceKit  
**Kind**: init

Creates a new account query structure with the provided sort descriptors and, optionally, a predicate and limit on the number of records the query should return.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
init(sortDescriptors: [SortDescriptor<Account>] = [], predicate: Predicate<Account>? = nil, limit: Int? = nil, offset: Int? = nil)
```

## Parameters

- `sortDescriptors`: An array of [`Account`](account.md) sort descriptors.
- `predicate`: A [`Predicate`](https://developer.apple.com/documentation/Foundation/Predicate) to filter the `Account` records with.
- `limit`: An integer that indicates the maximum number of `Account` records to return.
- `offset`: An integer that indicates the number of records to offset the result by.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/accountquery/init(sortdescriptors:predicate:limit:offset:))*