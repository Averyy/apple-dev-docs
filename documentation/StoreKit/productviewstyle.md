# ProductViewStyle

**Framework**: StoreKit  
**Kind**: protocol

A type that specifies the appearance and interaction of In-App Purchase products within the view hierarchy.

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
@preconcurrency protocol ProductViewStyle
```

#### Overview

To configure the in-app purchase product style for a view hierarchy, use the [`productViewStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/productViewStyle(_:)) modifier.

To create a custom style, declare a type that conforms to the `ProductViewStyle` protocol. Implement the [`makeBody(configuration:)`](productviewstyle/makebody(configuration:).md) method to return a view that composes the elements of the configuration that the system provides to your method. The following code example shows how to create a custom product view style:

```swift
struct CustomProductViewStyle: ProductViewStyle {
    func makeBody(configuration: Configuration) -> some View {
        switch configuration.state {
        // Add other cases here.
        case .success(let product):
            VStack(alignment: .center) {
                configuration.icon
                Text(product.displayName)
                Button(product.displayPrice) {}
            }
        }
    }
}

ProductView(id: "com.example.product")
    .productViewStyle(CustomProductViewStyle())
    // Add your code here.
```

## Topics

### Getting built-in product view styles
- [static var automatic: AutomaticProductViewStyle](productviewstyle/automatic.md)
- [static var compact: CompactProductViewStyle](productviewstyle/compact.md)
  An product view style suitable for layouts where less space is available, or for displaying more items in a small amount of space.
- [static var large: LargeProductViewStyle](productviewstyle/large.md)
  A product view style suitable for layouts where the in-app purchase content is prominent.
- [static var regular: RegularProductViewStyle](productviewstyle/regular.md)
  A product view style that uses a standard, platform-appropriate layout.
### Creating custom product views
- [func makeBody(configuration: Self.Configuration) -> Self.Body](productviewstyle/makebody(configuration:).md)
  Creates a view that represents the body of a product view.
- [ProductViewStyle.Configuration](productviewstyle/configuration.md)
  A type that represents the properties of a product view style.
- [associatedtype Body : View](productviewstyle/body.md)
  A view that represents the body of a product view.
### Supporting types
- [struct AutomaticProductViewStyle](automaticproductviewstyle.md)
- [struct CompactProductViewStyle](compactproductviewstyle.md)
  A style for a product view that’s suitable for layouts with less available space, or for displaying more items in a small amount of space.
- [struct RegularProductViewStyle](regularproductviewstyle.md)
  A style for a product view that uses a standard, platform-appropriate layout.
- [struct LargeProductViewStyle](largeproductviewstyle.md)
  A style for a product view that’s suitable for layouts where the in-app purchase content is prominent.

## Relationships

### Conforming Types
- [AutomaticProductViewStyle](automaticproductviewstyle.md)
- [CompactProductViewStyle](compactproductviewstyle.md)
- [LargeProductViewStyle](largeproductviewstyle.md)
- [RegularProductViewStyle](regularproductviewstyle.md)

## See Also

- [nonisolated func productViewStyle(_ style: some ProductViewStyle) -> some View
](../SwiftUI/View/productViewStyle(_:).md)
  Sets the style for In-App Purchase product views within a view.
- [nonisolated func productIconBorder() -> some View
](../SwiftUI/View/productIconBorder.md)
  Adds a standard border to an in-app purchase product’s icon .
- [struct ProductViewStyleConfiguration](productviewstyleconfiguration.md)
  The properties of an In-App Purchase product for use by custom product view styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/productviewstyle)*