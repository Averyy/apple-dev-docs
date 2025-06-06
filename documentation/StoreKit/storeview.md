# StoreView

**Framework**: StoreKit  
**Kind**: struct

A view that merchandises a collection of In-App Purchase products.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency struct StoreView<Icon, PlaceholderIcon> where Icon : View, PlaceholderIcon : View
```

#### Overview

A `StoreView` displays a collection of in-app purchase products, including their localized names, descriptions, and prices, and displays a purchase button.

Create a store view by providing a collection of product identifiers for the view to load from the App Store, or a collection of [`Product`](product.md) values you previously loaded. If you provide product identifiers, the store view automatically loads the product information from the App Store, and updates the view when the products are available.

You can provide a view to use as an icon or image for each individual product. If you provide product identifiers, you can optionally provide placeholder icons for the system to use instead of the automatic placeholder icon.

If you set up promoted images for your products in App Store Connect, you can choose to display those images for your products.

##### Manage the Store Layout

The `StoreView` arranges products in rows. If the view has enough horizontal space available, the store adds columns. In tvOS, the view arranges the products in columns and adds rows as space permits.

The store view grows to fit its container, and scrolls when the container doesn’t have enough space to display all the products. Use the [`fixedSize(horizontal:vertical:)`](https://developer.apple.com/documentation/SwiftUI/View/fixedSize(horizontal:vertical:)) modifier to change this behavior.

To achieve a custom layout, you can compose [`ProductView`](productview.md) instances with other container views instead of using the `StoreView`.

##### Customize the Store

You can customize the store by displaying additional buttons, and applying styles.

To display a button that syncs in-app purchase entitlements with the App Store, modify the in-app store view or an ancestor view using the `storeButton(_:for:)` modifier with the parameters [`Visibility.visible`](https://developer.apple.com/documentation/SwiftUI/Visibility/visible) and [`restorePurchases`](storebuttonkind/restorepurchases.md). The app calls the [`sync()`](appstore/sync().md) method when people use this button.

You can customize the appearance of the products using product view styles, such as [`CompactProductViewStyle`](compactproductviewstyle.md), [`LargeProductViewStyle`](largeproductviewstyle.md), and [`RegularProductViewStyle`](regularproductviewstyle.md). To apply the style, call the [`productViewStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/productViewStyle(_:)) modifier.

## Topics

### Creating store views that load products
- [init(ids: some Collection<String>, prefersPromotionalIcon: Bool)](storeview/init(ids:preferspromotionalicon:).md)
  Creates a view to load and merchandise a collection of products from the App Store using product identifiers.
- [init(ids: some Collection<String>, prefersPromotionalIcon: Bool, icon: (Product) -> Icon)](storeview/init(ids:preferspromotionalicon:icon:).md)
  Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using a custom image.
- [init(ids: some Collection<String>, prefersPromotionalIcon: Bool, icon: (Product) -> Icon, placeholderIcon: () -> PlaceholderIcon)](storeview/init(ids:preferspromotionalicon:icon:placeholdericon:).md)
  Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using an image and a custom placeholder icon.
- [init(ids: some Collection<String>, icon: (Product, ProductIconPhase) -> Icon, placeholderIcon: () -> PlaceholderIcon)](storeview/init(ids:icon:placeholdericon:).md)
  Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using their promotional images and a custom placeholder icon.
### Creating store views with preloaded products
- [init(products: some Collection<Product>, prefersPromotionalIcon: Bool)](storeview/init(products:preferspromotionalicon:).md)
  Creates a view to load and merchandise a collection of products from the App Store.
- [init(products: some Collection<Product>, prefersPromotionalIcon: Bool, icon: (Product) -> Icon)](storeview/init(products:preferspromotionalicon:icon:).md)
  Creates a view to merchandise a collection of products using a custom icon.
- [init(products: some Collection<Product>, icon: (Product, ProductIconPhase) -> Icon)](storeview/init(products:icon:).md)
  Creates a view to merchandise a collection of products with promotional images.
### Loading promotional images
- [enum ProductIconPhase](producticonphase.md)
  The current phase of the asynchronous loading operation of a product’s promotional image.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct ProductView](productview.md)
  A view that merchandises an individual In-App Purchase product.
- [struct SubscriptionStoreView](subscriptionstoreview.md)
  A view that merchandises a collection of auto-renewable subscription options that belong to the same subscription group.
- [Backyard Birds: Building an app with SwiftData and widgets](../SwiftUI/Backyard-birds-sample.md)
  Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storeview)*