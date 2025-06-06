# init(_:icon:)

**Framework**: StoreKit  
**Kind**: init

Creates a view to display a product that the system already loaded from the App Store, and merchandise it using its promotional image.

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
init(_ product: Product, @ViewBuilder icon: @escaping (ProductIconPhase) -> Icon) where PlaceholderIcon == EmptyView
```

#### Discussion

The product view asynchronously loads and displays the product’s promotional image.

The [`ProductIconPhase`](producticonphase.md) value indicates whether the promotional image is loading, unavailable, or whether it succeeded or failed to load. Use the [`ProductIconPhase`](producticonphase.md) to monitor current loading phase, and to decide the image to return in the `icon` closure.

## Parameters

- `product`: The product to merchandise.
- `icon`: A closure that receives a   as an input, which indicates the state of the loading operation of the product’s promoted image, and returns the view to display for the specified phase.

## See Also

- [init(Product, prefersPromotionalIcon: Bool, icon: () -> Icon)](productview/init(_:preferspromotionalicon:icon:).md)
  Creates a view to merchandise an individual product using a custom icon.
- [init(Product, prefersPromotionalIcon: Bool)](productview/init(_:preferspromotionalicon:).md)
  Creates a view to merchandise an individual product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/productview/init(_:icon:))*