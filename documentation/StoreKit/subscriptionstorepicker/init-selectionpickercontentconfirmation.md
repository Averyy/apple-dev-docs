# init(selection:pickerContent:confirmation:)

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
@preconcurrency init(selection: Binding<SubscriptionStoreControlStyleConfiguration.Option?>, @ViewBuilder pickerContent: () -> PickerContent, @ViewBuilder confirmation: @escaping (SubscriptionStoreControlStyleConfiguration.Option) -> ConfirmationContent)
```

## See Also

- [init(SubscriptionStoreControlStyleConfiguration, selection: Binding<SubscriptionStoreControlStyleConfiguration.Option?>, pickerOptionContent: (SubscriptionStoreControlStyleConfiguration.PickerOption) -> PickerContent, confirmation: (SubscriptionStoreControlStyleConfiguration.Option) -> ConfirmationContent)](subscriptionstorepicker/init(_:selection:pickeroptioncontent:confirmation:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorepicker/init(selection:pickercontent:confirmation:))*