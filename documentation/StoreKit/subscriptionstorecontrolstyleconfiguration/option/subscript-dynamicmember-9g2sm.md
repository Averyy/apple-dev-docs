# subscript(dynamicMember:)

**Framework**: StoreKit  
**Kind**: subscript

Facilitates accessing product properties on an option value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
subscript<T>(dynamicMember keyPath: KeyPath<Product, T>) -> T { get }
```

#### Discussion

You don’t use this subscript directly. Instead, access the properties of a [`Product`](product.md) instance directly on a [`SubscriptionStoreControlStyleConfiguration.Option`](subscriptionstorecontrolstyleconfiguration/option.md) value. For an example of using a dynamic member lookup, see [`SubscriptionStoreControlStyleConfiguration.Option`](subscriptionstorecontrolstyleconfiguration/option.md).

## See Also

- [subscript<T>(dynamicMember _: KeyPath<Product.SubscriptionInfo, T?>) -> T?](subscriptionstorecontrolstyleconfiguration/option/subscript(dynamicmember:)-8sl2m.md)
  Facilitates accessing optional subscription properties on an option value.
- [subscript<T>(dynamicMember _: KeyPath<Product.SubscriptionInfo, T>) -> T?](subscriptionstorecontrolstyleconfiguration/option/subscript(dynamicmember:)-wjww.md)
  Facilitates accessing subscription properties on an option value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/subscript(dynamicmember:)-9g2sm)*