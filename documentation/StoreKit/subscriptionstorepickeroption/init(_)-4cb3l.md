# init(_:)

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
@preconcurrency init(_ option: SubscriptionStoreControlStyleConfiguration.Option) where Label == AutomaticSubscriptionStorePickerOptionLabel
```

Available when `Label` conforms to `View`.

## See Also

### Creating a subscription picker option
- [init(SubscriptionStoreControlStyleConfiguration.PickerOption)](./init%28_%29-3iu97.md)
- [init(SubscriptionStoreControlStyleConfiguration.Option, label: (SubscriptionStoreControlStyleConfiguration.PickerOption) -> Label)](./init%28_,label%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorepickeroption/init(_:)-4cb3l)*