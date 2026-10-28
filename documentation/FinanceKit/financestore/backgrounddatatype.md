# FinanceStore.BackgroundDataType

**Framework**: FinanceKit  
**Kind**: enum  
**Role**: Enumeration

Types of data in the finance store supported by background delivery.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum BackgroundDataType
```

## Overview

When these types of data change in the finance store, any background delivery extension with updates enabled for them will be notified.

## Topics

### Enumeration Cases
- [FinanceStore.BackgroundDataType.accountBalances](./backgrounddatatype/accountbalances.md)
  Receive updates for changes to `AccountBalance`.
- [FinanceStore.BackgroundDataType.accounts](./backgrounddatatype/accounts.md)
  Receive updates for changes to `Account`.
- [FinanceStore.BackgroundDataType.transactions](./backgrounddatatype/transactions.md)
  Receive updates for changes to `Transaction`.

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
- [FinanceStore.UpdateFrequency](./updatefrequency.md)
  Frequencies of background delivery updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/backgrounddatatype)*