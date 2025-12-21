# FinanceStore.SaveOrderResult

**Framework**: FinanceKit  
**Kind**: enum

Result type for the finance store’s save order method.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum SaveOrderResult
```

## Topics

### Enumeration Cases
- [FinanceStore.SaveOrderResult.added](financestore/saveorderresult/added.md)
  The framework added the order to the finance store.
- [FinanceStore.SaveOrderResult.cancelled](financestore/saveorderresult/cancelled.md)
  The individual canceled the order.
- [FinanceStore.SaveOrderResult.newerExisting](financestore/saveorderresult/newerexisting.md)
  There’s a newer, existing order already in the finance store.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [FinanceStore.ContainsOrderResult](financestore/containsorderresult.md)
  Result type for queries against the finance store’s orders.
- [FinanceStore.DataType](financestore/datatype.md)
  Values that describe the kinds of data in the finance store.
- [FinanceStore.BackgroundDataType](financestore/backgrounddatatype.md)
  Types of data in the finance store supported by background delivery.
- [FinanceStore.UpdateFrequency](financestore/updatefrequency.md)
  Frequencies of background delivery updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/saveorderresult)*