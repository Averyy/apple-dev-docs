# init(_:prefersPromotionalIcon:)

**Framework**: StoreKit  
**Kind**: init

Creates a view to merchandise an individual product.

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
init(_ product: Product, prefersPromotionalIcon: Bool = true) where Icon == EmptyView, PlaceholderIcon == EmptyView
```

#### Discussion

If the product has a promotional image available, the view displays it. Otherwise, the view doesn’t show an image.

If you set the `prefersPromotionalIcon` parameter to `false`, the view doesn’t show an image even if the product has a promotional image available.

> 💡 **Tip**:  To gain more control over the image that decorates this view, use the [`init(_:icon:)`](productview/init(_:icon:).md) initializer. It receives a [`ProductIconPhase`](producticonphase.md), which enables you to supply an image for each phase of the image-loading process.

## Parameters

- `product`: The product to merchandise.
- `prefersPromotionalIcon`: A Boolean value that indicates whether to use the promotional image from the App Store, if it’s available. If this value is   and a promotional image for the product is available, the view displays it.

## See Also

- [init(Product, prefersPromotionalIcon: Bool, icon: () -> Icon)](productview/init(_:preferspromotionalicon:icon:).md)
  Creates a view to merchandise an individual product using a custom icon.
- [init(Product, icon: (ProductIconPhase) -> Icon)](productview/init(_:icon:).md)
  Creates a view to display a product that the system already loaded from the App Store, and merchandise it using its promotional image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/productview/init(_:preferspromotionalicon:))*