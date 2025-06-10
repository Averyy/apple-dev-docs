# disableBackgroundDelivery(for:)

**Framework**: FinanceKit  
**Kind**: method

Disables background delivery for the specified types.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func disableBackgroundDelivery(for types: [FinanceStore.BackgroundDataType])
```

#### Discussion

Your background delivery extension will no longer receive updates when data of the given types change in the finance store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/disablebackgrounddelivery(for:))*