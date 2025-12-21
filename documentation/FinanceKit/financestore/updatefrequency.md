# FinanceStore.UpdateFrequency

**Framework**: FinanceKit  
**Kind**: enum

Frequencies of background delivery updates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
enum UpdateFrequency
```

#### Overview

These represent the expected minimum interval between updates delivered to a `BackgroundDeliveryExtension` and if no data changes, no updates will occur. After an update is delivered, if data changes again within the interval, the next update won’t happen until the interval has passed.

> **Note**:  The window of time to process data is larger for longer update frequencies.

## Topics

### Enumeration Cases
- [FinanceStore.UpdateFrequency.daily](financestore/updatefrequency/daily.md)
  Get notified within a day of data updating.
- [FinanceStore.UpdateFrequency.hourly](financestore/updatefrequency/hourly.md)
  Get notified within an hour of data updating.
- [FinanceStore.UpdateFrequency.weekly](financestore/updatefrequency/weekly.md)
  Get notified within a week of data updating.

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
- [FinanceStore.BackgroundDataType](financestore/backgrounddatatype.md)
  Types of data in the finance store supported by background delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/updatefrequency)*