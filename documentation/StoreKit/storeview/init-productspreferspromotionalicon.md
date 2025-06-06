# init(products:prefersPromotionalIcon:)

**Framework**: StoreKit  
**Kind**: init

Creates a view to load and merchandise a collection of products from the App Store.

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
init(products: some Collection<Product>, prefersPromotionalIcon: Bool = false) where Icon == EmptyView, PlaceholderIcon == EmptyView
```

#### Discussion

By default, the store view doesn’t show promotional images. If you set `prefersPromotionalIcon` to `true`, the store view uses each product’s promotional image as its icon.

## Parameters

- `products`: The products to merchandise.
- `prefersPromotionalIcon`: A Boolean value that indicates whether to use promotional images from the App Store, if they’re available. If this parameter is  , the system ignores promotional images.

## See Also

- [init(products: some Collection<Product>, prefersPromotionalIcon: Bool, icon: (Product) -> Icon)](storeview/init(products:preferspromotionalicon:icon:).md)
  Creates a view to merchandise a collection of products using a custom icon.
- [init(products: some Collection<Product>, icon: (Product, ProductIconPhase) -> Icon)](storeview/init(products:icon:).md)
  Creates a view to merchandise a collection of products with promotional images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storeview/init(products:preferspromotionalicon:))*