# icon

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The subscription option’s icon.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var icon: SubscriptionStoreControlStyleConfiguration.Icon? { get }
```

#### Discussion

Use this property to access the icon you configure for a subscription option using the [`subscriptionStoreControlIcon(icon:)`](../../../SwiftUI/view/subscriptionstorecontrolicon%28icon%29.md) view modifier.

## See Also

### Getting properties of the subscription picker option
- [var subscription: Product](./subscription.md)
  The auto-renewable subscription that the picker option represents.
- [var activeOffer: Product.SubscriptionOffer?](./activeoffer.md)
- [let isSelected: Bool](./isselected.md)
  A Boolean value that indicates whether the picker option is in a selected state.
- [var id: Product.ID](./id.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/icon)*