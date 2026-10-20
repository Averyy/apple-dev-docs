# LargeProductViewStyle

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

A style for a product view that’s suitable for layouts where the Apple In-App Purchase content is prominent.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct LargeProductViewStyle
```

## Topics

### Getting the large product view style
- [static var large: LargeProductViewStyle](./productviewstyle/large.md)
  A product view style suitable for layouts where the Apple In-App Purchase content is prominent.
### Creating the style
- [init()](./largeproductviewstyle/init%28%29.md)

## Relationships

### Conforms To
- [ProductViewStyle](./productviewstyle.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [struct AutomaticProductViewStyle](./automaticproductviewstyle.md)
- [struct CompactProductViewStyle](./compactproductviewstyle.md)
  A style for a product view that’s suitable for layouts with less available space, or for displaying more items in a small amount of space.
- [struct RegularProductViewStyle](./regularproductviewstyle.md)
  A style for a product view that uses a standard, platform-appropriate layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/largeproductviewstyle)*