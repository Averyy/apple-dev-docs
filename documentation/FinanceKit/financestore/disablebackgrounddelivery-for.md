# disableBackgroundDelivery(for:)

**Framework**: FinanceKit  
**Kind**: method

Disables background delivery for the specified types.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func disableBackgroundDelivery(for types: [FinanceStore.BackgroundDataType])
```

#### Discussion

The app’s background delivery extension will no longer receive updates when data of the given types change in the finance store.

## Parameters

- `types`: The types of data to disable updates for.

## See Also

- [func disableAllBackgroundDelivery()](financestore/disableallbackgrounddelivery.md)
  Disables background delivery for all data types.
- [func enableBackgroundDelivery(for: [FinanceStore.BackgroundDataType], frequency: FinanceStore.UpdateFrequency)](financestore/enablebackgrounddelivery(for:frequency:).md)
  Enables background delivery for the specified types and frequency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/disablebackgrounddelivery(for:))*