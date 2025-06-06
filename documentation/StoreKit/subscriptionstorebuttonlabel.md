# SubscriptionStoreButtonLabel

**Framework**: StoreKit  
**Kind**: struct

The label of the subscribe button that a subscription store view uses.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct SubscriptionStoreButtonLabel
```

## Topics

### Instance Properties
- [var action: SubscriptionStoreButtonLabel](subscriptionstorebuttonlabel/action-swift.property.md)
- [var displayName: SubscriptionStoreButtonLabel](subscriptionstorebuttonlabel/displayname-swift.property.md)
- [var multiline: SubscriptionStoreButtonLabel](subscriptionstorebuttonlabel/multiline-swift.property.md)
- [var price: SubscriptionStoreButtonLabel](subscriptionstorebuttonlabel/price-swift.property.md)
- [var singleLine: SubscriptionStoreButtonLabel](subscriptionstorebuttonlabel/singleline-swift.property.md)
### Type Properties
- [static var action: SubscriptionStoreButtonLabel](subscriptionstorebuttonlabel/action-swift.type.property.md)
- [static var automatic: SubscriptionStoreButtonLabel](subscriptionstorebuttonlabel/automatic.md)
- [static var displayName: SubscriptionStoreButtonLabel](subscriptionstorebuttonlabel/displayname-swift.type.property.md)
- [static var multiline: SubscriptionStoreButtonLabel](subscriptionstorebuttonlabel/multiline-swift.type.property.md)
- [static var price: SubscriptionStoreButtonLabel](subscriptionstorebuttonlabel/price-swift.type.property.md)
- [static var singleLine: SubscriptionStoreButtonLabel](subscriptionstorebuttonlabel/singleline-swift.type.property.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [nonisolated func subscriptionStoreControlIcon(@ViewBuilder icon: @escaping (Product, Product.SubscriptionInfo) -> some View) -> some View
](../SwiftUI/View/subscriptionStoreControlIcon(icon:).md)
  Sets a view to use to decorate individual subscription options within a subscription store view.
- [nonisolated func subscriptionStorePickerItemBackground(_ backgroundStyle: some ShapeStyle) -> some View
](../SwiftUI/View/subscriptionStorePickerItemBackground(_:).md)
  Sets the background style for picker items of the subscription store view instances within a view.
- [nonisolated func subscriptionStorePickerItemBackground(_ backgroundStyle: some ShapeStyle, in shape: some Shape) -> some View
](../SwiftUI/View/subscriptionStorePickerItemBackground(_:in:).md)
  Sets the background shape and style for subscription store view picker items within a view.
- [nonisolated func subscriptionStoreButtonLabel(_ label: SubscriptionStoreButtonLabel) -> some View
](../SwiftUI/View/subscriptionStoreButtonLabel(_:).md)
  Configures subscription store view instances within a view to use the provided button label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorebuttonlabel)*