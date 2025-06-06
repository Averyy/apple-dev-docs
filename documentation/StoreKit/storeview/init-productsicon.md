# init(products:icon:)

**Framework**: StoreKit  
**Kind**: init

Creates a view to merchandise a collection of products with promotional images.

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
init(products: some Collection<Product>, @ViewBuilder icon: @escaping (Product, ProductIconPhase) -> Icon) where PlaceholderIcon == EmptyView
```

#### Discussion

The store view asynchronously loads and displays each product’s promotional image. Use the [`ProductIconPhase`](producticonphase.md) to monitor the current loading phase of the product’s promotional image, and provide an image for each phase. For more information about the loading phases, see [`ProductIconPhase`](producticonphase.md).

## Parameters

- `products`: The products to merchandise.
- `icon`: A closure that receives a   and a   as input. The   indicates the state of the loading operation of the product’s promotional image. The closure returns the view to display for the given product and phase value.

## See Also

- [init(products: some Collection<Product>, prefersPromotionalIcon: Bool)](storeview/init(products:preferspromotionalicon:).md)
  Creates a view to load and merchandise a collection of products from the App Store.
- [init(products: some Collection<Product>, prefersPromotionalIcon: Bool, icon: (Product) -> Icon)](storeview/init(products:preferspromotionalicon:icon:).md)
  Creates a view to merchandise a collection of products using a custom icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storeview/init(products:icon:))*