# init(pickerContent:confirmation:)

**Framework**: StoreKit  
**Kind**: init

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency init(@ViewBuilder pickerContent: () -> PickerContent, @ViewBuilder confirmation: @escaping (SubscriptionStoreControlStyleConfiguration.Option) -> ConfirmationContent)
```

## See Also

- [init(SubscriptionStoreControlStyleConfiguration, pickerOptionContent: (SubscriptionStoreControlStyleConfiguration.PickerOption) -> PickerContent, confirmation: (SubscriptionStoreControlStyleConfiguration.Option) -> ConfirmationContent)](subscriptionstorepicker/init(_:pickeroptioncontent:confirmation:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorepicker/init(pickercontent:confirmation:))*