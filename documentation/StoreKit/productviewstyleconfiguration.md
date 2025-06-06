# ProductViewStyleConfiguration

**Framework**: StoreKit  
**Kind**: struct

The properties of an In-App Purchase product for use by custom product view styles.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct ProductViewStyleConfiguration
```

#### Overview

Use the `ProductViewStyleConfiguration` to create a custom [`ProductViewStyle`](productviewstyle.md).

## Topics

### Getting a product’s information
- [var product: Product?](productviewstyleconfiguration/product.md)
  The in-app purchase product to merchandise.
- [let state: Product.TaskState](productviewstyleconfiguration/state.md)
  The product task state that indicates the product’s loading phase.
- [let hasCurrentEntitlement: Bool](productviewstyleconfiguration/hascurrententitlement.md)
  A Boolean value that indicates whether an in-app purchase transaction exists for the product.
### Getting a product view’s icon
- [let icon: ProductViewStyleConfiguration.Icon](productviewstyleconfiguration/icon-swift.property.md)
  A decorative view for merchandising the product.
- [ProductViewStyleConfiguration.Icon](productviewstyleconfiguration/icon-swift.struct.md)
  A type-erased icon of an in-app purchase product.
### Getting a product’s description visibility
- [let descriptionVisibility: Visibility](productviewstyleconfiguration/descriptionvisibility.md)
  The visibility of product descriptions.
### Initiating a purchase
- [func purchase()](productviewstyleconfiguration/purchase.md)
  Initiates a purchase action for the product.

## See Also

- [nonisolated func productViewStyle(_ style: some ProductViewStyle) -> some View
](../SwiftUI/View/productViewStyle(_:).md)
  Sets the style for In-App Purchase product views within a view.
- [nonisolated func productIconBorder() -> some View
](../SwiftUI/View/productIconBorder.md)
  Adds a standard border to an in-app purchase product’s icon .
- [protocol ProductViewStyle](productviewstyle.md)
  A type that specifies the appearance and interaction of In-App Purchase products within the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/productviewstyleconfiguration)*