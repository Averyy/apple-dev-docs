# init(id:prefersPromotionalIcon:icon:)

**Framework**: StoreKit  
**Kind**: init

Creates a view to load an individual product from the App Store and merchandise it using a custom icon.

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
init(id productID: Product.ID, prefersPromotionalIcon: Bool = false, @ViewBuilder icon: () -> Icon) where PlaceholderIcon == AutomaticProductPlaceholderIcon
```

#### Discussion

The product view displays a placeholder icon until the system finishes loading the product. After the product loads, the system uses the view you provide in the `icon` parameter, by default. If `prefersPromotionalIcon` is `true` and the product has a promotional image, the view displays the promotional image as its icon instead of the provided view.

> 💡 **Tip**:  To gain more control over the image that decorates this view, use the [`init(id:icon:placeholderIcon:)`](productview/init(id:icon:placeholdericon:).md) initializer. It receives a [`ProductIconPhase`](producticonphase.md), which enables you to supply an image for each phase of the image-loading process.

## Parameters

- `productID`: The product identifier to load from the App Store.
- `prefersPromotionalIcon`: A Boolean value that indicates whether to use the promotional image from the App Store, if it’s available. If this value is   and a promotional image for the product is available, the view displays it instead of the view you provide in the   parameter.
- `icon`: A closure that returns the image the view displays when the system finishes loading the product from the App Store.

## See Also

- [init(id: Product.ID, prefersPromotionalIcon: Bool)](productview/init(id:preferspromotionalicon:).md)
  Creates a view to load and merchandise an individual product from the App Store.
- [init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon, placeholderIcon: () -> PlaceholderIcon)](productview/init(id:preferspromotionalicon:icon:placeholdericon:).md)
  Creates a view to load an individual product from the App Store and merchandise it using an image and a custom placeholder icon.
- [init(id: Product.ID, icon: (ProductIconPhase) -> Icon, placeholderIcon: () -> PlaceholderIcon)](productview/init(id:icon:placeholdericon:).md)
  Creates a view to load an individual product from the App Store, and merchandise it using its promotional image and a custom placeholder icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/productview/init(id:preferspromotionalicon:icon:))*