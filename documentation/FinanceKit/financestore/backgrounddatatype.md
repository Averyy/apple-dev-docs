# FinanceStore.BackgroundDataType

**Framework**: FinanceKit  
**Kind**: enum

Types of data in the finance store supported by background delivery.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
enum BackgroundDataType
```

#### Overview

When these types of data change in the finance store, any background delivery extension with updates enabled for them will be notified.

## Topics

### Enumeration Cases
- [FinanceStore.BackgroundDataType.accountBalances](financestore/backgrounddatatype/accountbalances.md)
  Receive updates for changes to `AccountBalance`.
- [FinanceStore.BackgroundDataType.accounts](financestore/backgrounddatatype/accounts.md)
  Receive updates for changes to `Account`.
- [FinanceStore.BackgroundDataType.transactions](financestore/backgrounddatatype/transactions.md)
  Receive updates for changes to `Transaction`.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [FinanceStore.ContainsOrderResult](financestore/containsorderresult.md)
  Result type for queries against the finance store’s orders.
- [FinanceStore.DataType](financestore/datatype.md)
  Values that describe the kinds of data in the finance store.
- [FinanceStore.SaveOrderResult](financestore/saveorderresult.md)
  Result type for the finance store’s save order method.
- [FinanceStore.UpdateFrequency](financestore/updatefrequency.md)
  Frequencies of background delivery updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/backgrounddatatype)*