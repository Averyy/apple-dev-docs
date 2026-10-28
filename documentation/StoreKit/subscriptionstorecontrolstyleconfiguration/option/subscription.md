# subscription

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The auto-renewable subscription to merchandise.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var subscription: Product { get }
```

## Discussion

[`SubscriptionStoreControlStyleConfiguration.Option`](../option.md) is a dynamic member lookup type, which code refers to as `Option` when it’s a nested type. You don’t need to use the [`subscription`](./subscription.md) property directly to access the properties of the [`Product`](../../product.md) value. Instead, access any properties of [`Product`](../../product.md) or [`Product.SubscriptionInfo`](../../product/subscriptioninfo.md) directly on the `Option` value.

The following code example creates a button for each subscription option and displays its name. The [`displayName`](../../product/displayname.md) property is available on [`SubscriptionStoreControlStyleConfiguration.Option`](../option.md) to use as the button label.

```swift
struct DisplayNameButtonsControlStyle: SubscriptionStoreControlStyle {

    func makeBody(configuration: Configuration) -> some View {
        ForEach(configuration.options) { option in
            Button(option.displayName, action: option.subscribe)
        }
    }
}
```

> ❗ **Important**:  Use the [`subscribe()`](./subscribe%28%29.md) method on the [`SubscriptionStoreControlStyleConfiguration.Option`](../option.md) value when a customer initiates a purchase. Don’t use [`purchase(confirmIn:options:)`](../../product/purchase%28confirmin,options%29-6dj6y.md) or related purchase methods on this property for initiating a purchase.

## See Also

### Getting the subscription product and offer
- [var id: Product.ID](./id.md)
  The product ID of the auto-renewable subscription.
- [var activeOffer: Product.SubscriptionOffer?](./activeoffer.md)
  The subscription offer the customer is eligible for, and that applies to the subscription option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/subscription)*