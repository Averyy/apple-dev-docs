# disableAllBackgroundDelivery()

**Framework**: FinanceKit  
**Kind**: method  
**Role**: Instance Method

Disables background delivery for all data types.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func disableAllBackgroundDelivery()
```

#### Discussion

The app’s background delivery extension will no longer receive updates when data changes in the finance store.

## See Also

### Instance Methods
- [func disableBackgroundDelivery(for: [FinanceStore.BackgroundDataType])](./disablebackgrounddelivery%28for%29.md)
  Disables background delivery for the specified types.
- [func enableBackgroundDelivery(for: [FinanceStore.BackgroundDataType], frequency: FinanceStore.UpdateFrequency)](./enablebackgrounddelivery%28for,frequency%29.md)
  Enables background delivery for the specified types and frequency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/disableallbackgrounddelivery())*