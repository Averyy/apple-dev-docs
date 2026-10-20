# init(selection:pickerContent:confirmation:)

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency init(selection: Binding<SubscriptionStoreControlStyleConfiguration.Option?>, @ViewBuilder pickerContent: () -> PickerContent, @ViewBuilder confirmation: @escaping (SubscriptionStoreControlStyleConfiguration.Option) -> ConfirmationContent)
```

Available when `PickerContent` conforms to `View` and `ConfirmationContent` conforms to `View`.

## See Also

### Managing a subscription picker’s selection state
- [init(SubscriptionStoreControlStyleConfiguration, selection: Binding<SubscriptionStoreControlStyleConfiguration.Option?>, pickerOptionContent: (SubscriptionStoreControlStyleConfiguration.PickerOption) -> PickerContent, confirmation: (SubscriptionStoreControlStyleConfiguration.Option) -> ConfirmationContent)](./init%28_,selection,pickeroptioncontent,confirmation%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorepicker/init(selection:pickercontent:confirmation:))*