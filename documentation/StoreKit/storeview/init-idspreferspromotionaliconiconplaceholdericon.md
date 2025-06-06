# init(ids:prefersPromotionalIcon:icon:placeholderIcon:)

**Framework**: StoreKit  
**Kind**: init

Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using an image and a custom placeholder icon.

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
init(ids productIDs: some Collection<String>, prefersPromotionalIcon: Bool = false, @ViewBuilder icon: @escaping (Product) -> Icon, @ViewBuilder placeholderIcon: () -> PlaceholderIcon)
```

#### Discussion

The store view shows the custom placeholder icon until all products finish loading. After the view finishes loading the products, it uses the image you provide, by default. If you set `prefersPromotionalIcon` to `true`, any products that have an available promotional image use the promotional image instead.

The following example shows how to create a store view using an icon and a custom placeholder icon:

```swift
StoreView(ids: [
    "com.example.product1",
    "com.example.product2"
]) { product in
     Image(systemName: "star.fill")
         .foregroundStyle(.yellow)
 } placeholderIcon: {
      Image(systemName: "star.fill")
         .foregroundStyle(.gray)
 }
```

## Parameters

- `productIDs`: The product identifiers to load from the App Store.
- `prefersPromotionalIcon`: A Boolean value that indicates whether to use a promotional image from the App Store, if it’s available. If this parameter is  , the system ignores promotional images.
- `icon`: A closure that returns the image the view displays when the products finish loading from the App Store.
- `placeholderIcon`: A closure that returns the image that the view uses while the products are loading. The view uses the same placeholder image for all the products.

## See Also

- [init(ids: some Collection<String>, prefersPromotionalIcon: Bool)](storeview/init(ids:preferspromotionalicon:).md)
  Creates a view to load and merchandise a collection of products from the App Store using product identifiers.
- [init(ids: some Collection<String>, prefersPromotionalIcon: Bool, icon: (Product) -> Icon)](storeview/init(ids:preferspromotionalicon:icon:).md)
  Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using a custom image.
- [init(ids: some Collection<String>, icon: (Product, ProductIconPhase) -> Icon, placeholderIcon: () -> PlaceholderIcon)](storeview/init(ids:icon:placeholdericon:).md)
  Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using their promotional images and a custom placeholder icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storeview/init(ids:preferspromotionalicon:icon:placeholdericon:))*