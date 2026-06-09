# init(sortDescriptors:predicate:limit:offset:)

**Framework**: FinanceKit  
**Kind**: init

Creates a new account balance query structure with the provided sort descriptors.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
init(sortDescriptors: [SortDescriptor<AccountBalance>] = [], predicate: Predicate<AccountBalance>? = nil, limit: Int? = nil, offset: Int? = nil)
```

## Parameters

- `sortDescriptors`: An array of [`AccountBalance`](accountbalance.md) sort descriptors.
- `predicate`: A [`Predicate`](https://developer.apple.com/documentation/Foundation/Predicate) to filter the `Account` records with.
- `limit`: An integer that indicates the maximum number of  records to return.
- `offset`: An integer that indicates the number of records to offset the result by.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/accountbalancequery/init(sortdescriptors:predicate:limit:offset:))*