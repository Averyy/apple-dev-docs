# init(ids:icon:placeholderIcon:)

**Framework**: StoreKit  
**Kind**: init

Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using their promotional images and a custom placeholder icon.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(ids productIDs: some Collection<String>, @ViewBuilder icon: @escaping (Product, ProductIconPhase) -> Icon, @ViewBuilder placeholderIcon: () -> PlaceholderIcon)
```

#### Discussion

The store view shows the custom `placeholderIcon` until all products finish loading. After the products finish loading, the view asynchronously loads and displays each product’s promotional image.

Use the [`ProductIconPhase`](producticonphase.md) to monitor the current loading state of a product’s promotional image, and provide a view for each phase. Consider returning the view provided in the `placeholderIcon` closure for during the [`ProductIconPhase.loading`](producticonphase/loading.md) phase. For more information, see [`ProductIconPhase`](producticonphase.md).

If a product is unavailable, the store view uses the view that the `placeholderIcon` closure provides as a fallback.

## Parameters

- `productIDs`: The product identifiers to load from the App Store.
- `icon`: A closure that receives a   and a   as input. The   indicates the state of the loading operation of the product’s promotional image. The closure returns the view to display for the given product and phase value.
- `placeholderIcon`: A closure that returns the view that the store view uses while the products are loading. The store view uses the same placeholder image for all the products.

## See Also

- [init(ids: some Collection<String>, prefersPromotionalIcon: Bool)](storeview/init(ids:preferspromotionalicon:).md)
  Creates a view to load and merchandise a collection of products from the App Store using product identifiers.
- [init(ids: some Collection<String>, prefersPromotionalIcon: Bool, icon: (Product) -> Icon)](storeview/init(ids:preferspromotionalicon:icon:).md)
  Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using a custom image.
- [init(ids: some Collection<String>, prefersPromotionalIcon: Bool, icon: (Product) -> Icon, placeholderIcon: () -> PlaceholderIcon)](storeview/init(ids:preferspromotionalicon:icon:placeholdericon:).md)
  Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using an image and a custom placeholder icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storeview/init(ids:icon:placeholdericon:))*