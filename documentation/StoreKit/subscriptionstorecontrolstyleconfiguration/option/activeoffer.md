# activeOffer

**Framework**: StoreKit  
**Kind**: property

The subscription offer the customer is eligible for, and that applies to the subscription option.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var activeOffer: Product.SubscriptionOffer? { get }
```

#### Discussion

Always display the terms of this subscription offer along with your control because it represents the offer that StoreKit automatically applies when you call the [`subscribe()`](subscriptionstorecontrolstyleconfiguration/option/subscribe().md) method. If the [`activeOffer`](subscriptionstorecontrolstyleconfiguration/option/activeoffer.md) property is `nil`, there’s no subscription offer.

> ❗ **Important**:  Don’t display offers from properties of [`subscription`](subscriptionstorecontrolstyleconfiguration/option/subscription.md), such as [`introductoryOffer`](product/subscriptioninfo/introductoryoffer.md).

The [`preferredSubscriptionOffer(_:)`](https://developer.apple.com/documentation/SwiftUI/View/preferredSubscriptionOffer(_:)) and [`subscriptionPromotionalOffer(offer:signature:)`](https://developer.apple.com/documentation/SwiftUI/View/subscriptionPromotionalOffer(offer:signature:)) view modifiers influence the [`offer`](purchaseintent/offer.md) property.

## See Also

- [var subscription: Product](subscriptionstorecontrolstyleconfiguration/option/subscription.md)
  The auto-renewable subscription to merchandise.
- [var id: Product.ID](subscriptionstorecontrolstyleconfiguration/option/id.md)
  The product ID of the auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/activeoffer)*