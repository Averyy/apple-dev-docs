# FinanceStore.UpdateFrequency

**Framework**: FinanceKit  
**Kind**: enum  
**Role**: Enumeration

Frequencies of background delivery updates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum UpdateFrequency
```

## Overview

These represent the expected minimum interval between updates delivered to a `BackgroundDeliveryExtension` and if no data changes, no updates will occur. After an update is delivered, if data changes again within the interval, the next update won’t happen until the interval has passed.

> **Note**:  The window of time to process data is larger for longer update frequencies.

## Topics

### Enumeration Cases
- [FinanceStore.UpdateFrequency.daily](./updatefrequency/daily.md)
  Get notified within a day of data updating.
- [FinanceStore.UpdateFrequency.hourly](./updatefrequency/hourly.md)
  Get notified within an hour of data updating.
- [FinanceStore.UpdateFrequency.weekly](./updatefrequency/weekly.md)
  Get notified within a week of data updating.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
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
- [FinanceStore.SaveOrderResult](./saveorderresult.md)
  Result type for the finance store’s save order method.
- [FinanceStore.BackgroundDataType](./backgrounddatatype.md)
  Types of data in the finance store supported by background delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/updatefrequency)*