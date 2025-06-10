# enableBackgroundDelivery(for:frequency:)

**Framework**: FinanceKit  
**Kind**: method

Enables background delivery for the specified types and frequency.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func enableBackgroundDelivery(for types: [FinanceStore.BackgroundDataType], frequency: FinanceStore.UpdateFrequency)
```

#### Discussion

Your background delivery extension will receive updates at the specified frequency when data of the given types change in the finance store. Subsequent calls with the same type will update the delivery frequency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/enablebackgrounddelivery(for:frequency:))*