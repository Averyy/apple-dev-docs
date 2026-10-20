# FinanceStore.SaveOrderResult

**Framework**: FinanceKit  
**Kind**: enum  
**Role**: Enumeration

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
- [FinanceStore.SaveOrderResult.added](./saveorderresult/added.md)
  The framework added the order to the finance store.
- [FinanceStore.SaveOrderResult.cancelled](./saveorderresult/cancelled.md)
  The individual canceled the order.
- [FinanceStore.SaveOrderResult.newerExisting](./saveorderresult/newerexisting.md)
  There’s a newer, existing order already in the finance store.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [FinanceStore.ContainsOrderResult](./containsorderresult.md)
  Result type for queries against the finance store’s orders.
- [FinanceStore.DataType](./datatype.md)
  Values that describe the kinds of data in the finance store.
- [FinanceStore.BackgroundDataType](./backgrounddatatype.md)
  Types of data in the finance store supported by background delivery.
- [FinanceStore.UpdateFrequency](./updatefrequency.md)
  Frequencies of background delivery updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/saveorderresult)*