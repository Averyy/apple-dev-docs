# subscription

**Framework**: StoreKit  
**Kind**: property

The auto-renewable subscription to merchandise.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var subscription: Product { get }
```

#### Discussion

[`SubscriptionStoreControlStyleConfiguration.Option`](subscriptionstorecontrolstyleconfiguration/option.md) is a dynamic member lookup type, which code refers to as `Option` when it’s a nested type. You don’t need to use the [`subscription`](subscriptionstorecontrolstyleconfiguration/option/subscription.md) property directly to access the properties of the [`Product`](product.md) value. Instead, access any properties of [`Product`](product.md) or [`Product.SubscriptionInfo`](product/subscriptioninfo.md) directly on the `Option` value.

The following code example creates a button for each subscription option and displays its name. The [`displayName`](product/displayname.md) property is available on [`SubscriptionStoreControlStyleConfiguration.Option`](subscriptionstorecontrolstyleconfiguration/option.md) to use as the button label.

```swift
struct DisplayNameButtonsControlStyle: SubscriptionStoreControlStyle {

    func makeBody(configuration: Configuration) -> some View {
        ForEach(configuration.options) { option in
            Button(option.displayName, action: option.subscribe)
        }
    }
}
```

> ❗ **Important**:  Use the [`subscribe()`](subscriptionstorecontrolstyleconfiguration/option/subscribe().md) method on the [`SubscriptionStoreControlStyleConfiguration.Option`](subscriptionstorecontrolstyleconfiguration/option.md) value when a customer initiates a purchase. Don’t use `Product/purchase(confirmIn:options:)` or related purchase methods on this property for initiating a purchase.

 Use the [`subscribe()`](subscriptionstorecontrolstyleconfiguration/option/subscribe().md) method on the [`SubscriptionStoreControlStyleConfiguration.Option`](subscriptionstorecontrolstyleconfiguration/option.md) value when a customer initiates a purchase. Don’t use `Product/purchase(confirmIn:options:)` or related purchase methods on this property for initiating a purchase.

## See Also

- [var id: Product.ID](subscriptionstorecontrolstyleconfiguration/option/id.md)
  The product ID of the auto-renewable subscription.
- [var activeOffer: Product.SubscriptionOffer?](subscriptionstorecontrolstyleconfiguration/option/activeoffer.md)
  The subscription offer the customer is eligible for, and that applies to the subscription option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/subscription)*