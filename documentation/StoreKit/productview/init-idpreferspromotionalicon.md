# init(id:prefersPromotionalIcon:)

**Framework**: StoreKit  
**Kind**: init

Creates a view to load and merchandise an individual product from the App Store.

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
init(id productID: Product.ID, prefersPromotionalIcon: Bool = false) where Icon == EmptyView, PlaceholderIcon == EmptyView
```

#### Discussion

By default, the view doesn’t show an icon. If you set the `prefersPromotionalIcon` parameter to `true`, the view displays a placeholder icon while loading, and replaces the placeholder with the promotional image for the product.

> 💡 **Tip**:  To gain more control over the image that decorates this view, use the [`init(id:icon:placeholderIcon:)`](productview/init(id:icon:placeholdericon:).md) initializer. It receives a [`ProductIconPhase`](producticonphase.md), which enables you to supply an image for each phase of the image-loading process.

 To gain more control over the image that decorates this view, use the [`init(id:icon:placeholderIcon:)`](productview/init(id:icon:placeholdericon:).md) initializer. It receives a [`ProductIconPhase`](producticonphase.md), which enables you to supply an image for each phase of the image-loading process.

## Parameters

- `productID`: The product identifier to load from the App Store.
- `prefersPromotionalIcon`: A Boolean value that indicates whether to use the promotional image from the App Store, if it’s available. If this parameter is  , the system ignores any promotional images.

## See Also

- [init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon)](productview/init(id:preferspromotionalicon:icon:).md)
  Creates a view to load an individual product from the App Store and merchandise it using a custom icon.
- [init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon, placeholderIcon: () -> PlaceholderIcon)](productview/init(id:preferspromotionalicon:icon:placeholdericon:).md)
  Creates a view to load an individual product from the App Store and merchandise it using an image and a custom placeholder icon.
- [init(id: Product.ID, icon: (ProductIconPhase) -> Icon, placeholderIcon: () -> PlaceholderIcon)](productview/init(id:icon:placeholdericon:).md)
  Creates a view to load an individual product from the App Store, and merchandise it using its promotional image and a custom placeholder icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/productview/init(id:preferspromotionalicon:))*