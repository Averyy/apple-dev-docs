# disableAllBackgroundDelivery()

**Framework**: FinanceKit  
**Kind**: method

Disables background delivery for all data types.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func disableAllBackgroundDelivery()
```

#### Discussion

The app’s background delivery extension will no longer receive updates when data changes in the finance store.

## See Also

- [func disableBackgroundDelivery(for: [FinanceStore.BackgroundDataType])](financestore/disablebackgrounddelivery(for:).md)
  Disables background delivery for the specified types.
- [func enableBackgroundDelivery(for: [FinanceStore.BackgroundDataType], frequency: FinanceStore.UpdateFrequency)](financestore/enablebackgrounddelivery(for:frequency:).md)
  Enables background delivery for the specified types and frequency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/disableallbackgrounddelivery())*