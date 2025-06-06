# init(id:icon:placeholderIcon:)

**Framework**: StoreKit  
**Kind**: init

Creates a view to load an individual product from the App Store, and merchandise it using its promotional image and a custom placeholder icon.

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
init(id productID: Product.ID, @ViewBuilder icon: @escaping (ProductIconPhase) -> Icon, @ViewBuilder placeholderIcon: () -> PlaceholderIcon)
```

#### Discussion

The product view shows the `placeholderIcon` until the system finishes loading the product. After the product finishes loading, the view asynchronously loads and displays the product’s promotional image. Use the [`ProductIconPhase`](producticonphase.md) to monitor the current loading state of the product’s promotional image.

If the product is unavailable, the view displays the `placeholderIcon` as a fallback.

The [`ProductIconPhase`](producticonphase.md) value indicates whether the promotional image is loading, unavailable, or whether it succeeded or failed to load. Use the phase to decide what to draw. While the image’s loading operation is in the [`ProductIconPhase.loading`](producticonphase/loading.md) phase, consider displaying the same view that you provide in the `placeholderIcon` closure. For more information, see [`ProductIconPhase`](producticonphase.md).

## Parameters

- `productID`: The product identifier to load from the App Store.
- `icon`: A closure that receives a   as an input, which indicates the state of the loading operation of the product’s promotional image, and returns the view to display for the specified phase.
- `placeholderIcon`: A closure that returns an icon to display until the system finishes loading the product from the App Store.

## See Also

- [init(id: Product.ID, prefersPromotionalIcon: Bool)](productview/init(id:preferspromotionalicon:).md)
  Creates a view to load and merchandise an individual product from the App Store.
- [init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon)](productview/init(id:preferspromotionalicon:icon:).md)
  Creates a view to load an individual product from the App Store and merchandise it using a custom icon.
- [init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon, placeholderIcon: () -> PlaceholderIcon)](productview/init(id:preferspromotionalicon:icon:placeholdericon:).md)
  Creates a view to load an individual product from the App Store and merchandise it using an image and a custom placeholder icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/productview/init(id:icon:placeholdericon:))*