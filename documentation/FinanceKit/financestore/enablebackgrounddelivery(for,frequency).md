# enableBackgroundDelivery(for:frequency:)

**Framework**: FinanceKit  
**Kind**: method  
**Role**: Instance Method

Enables background delivery for the specified types and frequency.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func enableBackgroundDelivery(for types: [FinanceStore.BackgroundDataType], frequency: FinanceStore.UpdateFrequency)
```

## Discussion

The app’s background delivery extension will receive updates at the specified frequency when data of the given types change in the finance store.

> **Note**:  Subsequent calls with the same type will update the delivery frequency.

## Parameters

- `types`: The types of data to enable updates for.
- `frequency`: The frequency at which updates should occur.

## See Also

### Instance Methods
- [func disableAllBackgroundDelivery()](./disableallbackgrounddelivery%28%29.md)
  Disables background delivery for all data types.
- [func disableBackgroundDelivery(for: [FinanceStore.BackgroundDataType])](./disablebackgrounddelivery%28for%29.md)
  Disables background delivery for the specified types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/enablebackgrounddelivery(for:frequency:))*