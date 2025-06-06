# subscript(dynamicMember:)

**Framework**: StoreKit  
**Kind**: subscript

Facilitates accessing product properties on a picker option value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
subscript<T>(dynamicMember keyPath: KeyPath<Product, T>) -> T { get }
```

#### Discussion

You don’t use this subscript directly. Instead, access the properties of a [`Product`](product.md) instance directly on a [`SubscriptionStoreControlStyleConfiguration.PickerOption`](subscriptionstorecontrolstyleconfiguration/pickeroption.md) value.

## See Also

- [subscript<T>(dynamicMember _: KeyPath<Product.SubscriptionInfo, T?>) -> T?](subscriptionstorecontrolstyleconfiguration/pickeroption/subscript(dynamicmember:)-2ahxy.md)
  Facilitates accessing optional subscription properties on a picker option value.
- [subscript<T>(dynamicMember _: KeyPath<Product.SubscriptionInfo, T>) -> T?](subscriptionstorecontrolstyleconfiguration/pickeroption/subscript(dynamicmember:)-4f3i1.md)
  Facilitates accessing subscription properties on a picker option value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/subscript(dynamicmember:)-8bsxh)*