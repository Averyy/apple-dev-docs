# FinanceStore.ContainsOrderResult

**Framework**: FinanceKit  
**Kind**: enum

Result type for queries against the finance store’s orders.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum ContainsOrderResult
```

#### Overview

These values represent the possible results of the `containsOrder` method you use to check whether an order you specified exists in the `FinanceStore`.

## Topics

### Enumeration Cases
- [FinanceStore.ContainsOrderResult.exists](financestore/containsorderresult/exists.md)
  The specified order exists.
- [FinanceStore.ContainsOrderResult.newerExists](financestore/containsorderresult/newerexists.md)
  A newer order than the one you specified exists.
- [FinanceStore.ContainsOrderResult.notFound](financestore/containsorderresult/notfound.md)
  The specified order doesn’t exist.
- [FinanceStore.ContainsOrderResult.olderExists](financestore/containsorderresult/olderexists.md)
  A older order than the one you specified exists.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [FinanceStore.DataType](financestore/datatype.md)
  Values that describe the kinds of data in the finance store.
- [FinanceStore.SaveOrderResult](financestore/saveorderresult.md)
  Result type for the finance store’s save order method.
- [FinanceStore.BackgroundDataType](financestore/backgrounddatatype.md)
  Types of data in the finance store supported by background delivery.
- [FinanceStore.UpdateFrequency](financestore/updatefrequency.md)
  Frequencies of background delivery updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/containsorderresult)*