# init(products:prefersPromotionalIcon:icon:)

**Framework**: StoreKit  
**Kind**: init

Creates a view to merchandise a collection of products using a custom icon.

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
init(products: some Collection<Product>, prefersPromotionalIcon: Bool = false, @ViewBuilder icon: @escaping (Product) -> Icon) where PlaceholderIcon == EmptyView
```

#### Discussion

If you set `prefersPromotionalIcon` to `true`, the view uses promotional images for products that have a promotional image available.

The following code example shows how to create a store view using a custom icon:

```swift
StoreView(products: [
          product1,
          product2,
          // Add products as needed.
 ]) { product in
    Image(systemName: "star.fill")
        .foregroundStyle(.yellow)
    }  
```

## Parameters

- `products`: The products to merchandise.
- `prefersPromotionalIcon`: A Boolean value that indicates whether to use promotional images from the App Store, if they’re available. If this parameter is  , the system ignores promotional images.
- `icon`: A closure that returns the image the view displays when the products finish loading from the App Store.

## See Also

- [init(products: some Collection<Product>, prefersPromotionalIcon: Bool)](storeview/init(products:preferspromotionalicon:).md)
  Creates a view to load and merchandise a collection of products from the App Store.
- [init(products: some Collection<Product>, icon: (Product, ProductIconPhase) -> Icon)](storeview/init(products:icon:).md)
  Creates a view to merchandise a collection of products with promotional images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storeview/init(products:preferspromotionalicon:icon:))*