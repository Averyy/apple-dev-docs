# FinanceStore.ContainsOrderResult

**Framework**: FinanceKit  
**Kind**: enum  
**Role**: Enumeration

Result type for queries against the finance store’s orders.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum ContainsOrderResult
```

## Overview

These values represent the possible results of the `containsOrder` method you use to check whether an order you specified exists in the `FinanceStore`.

## Topics

### Enumeration Cases
- [FinanceStore.ContainsOrderResult.exists](./containsorderresult/exists.md)
  The specified order exists.
- [FinanceStore.ContainsOrderResult.newerExists](./containsorderresult/newerexists.md)
  A newer order than the one you specified exists.
- [FinanceStore.ContainsOrderResult.notFound](./containsorderresult/notfound.md)
  The specified order doesn’t exist.
- [FinanceStore.ContainsOrderResult.olderExists](./containsorderresult/olderexists.md)
  A older order than the one you specified exists.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [FinanceStore.DataType](./datatype.md)
  Values that describe the kinds of data in the finance store.
- [FinanceStore.SaveOrderResult](./saveorderresult.md)
  Result type for the finance store’s save order method.
- [FinanceStore.BackgroundDataType](./backgrounddatatype.md)
  Types of data in the finance store supported by background delivery.
- [FinanceStore.UpdateFrequency](./updatefrequency.md)
  Frequencies of background delivery updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/containsorderresult)*