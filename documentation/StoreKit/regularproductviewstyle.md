# RegularProductViewStyle

**Framework**: StoreKit  
**Kind**: struct

A style for a product view that uses a standard, platform-appropriate layout.

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
@preconcurrency struct RegularProductViewStyle
```

## Topics

### Getting the regular product view style
- [static var regular: RegularProductViewStyle](productviewstyle/regular.md)
  A product view style that uses a standard, platform-appropriate layout.
### Creating the style
- [init()](regularproductviewstyle/init.md)
  Creates a regular product view style.

## Relationships

### Conforms To
- [ProductViewStyle](productviewstyle.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AutomaticProductViewStyle](automaticproductviewstyle.md)
- [struct CompactProductViewStyle](compactproductviewstyle.md)
  A style for a product view that’s suitable for layouts with less available space, or for displaying more items in a small amount of space.
- [struct LargeProductViewStyle](largeproductviewstyle.md)
  A style for a product view that’s suitable for layouts where the in-app purchase content is prominent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/regularproductviewstyle)*