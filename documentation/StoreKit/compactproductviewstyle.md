# CompactProductViewStyle

**Framework**: StoreKit  
**Kind**: struct

A style for a product view that’s suitable for layouts with less available space, or for displaying more items in a small amount of space.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
@MainActor
@preconcurrency struct CompactProductViewStyle
```

## Topics

### Getting the compact product view style
- [static var compact: CompactProductViewStyle](productviewstyle/compact.md)
  An product view style suitable for layouts where less space is available, or for displaying more items in a small amount of space.
### Creating the style
- [init()](compactproductviewstyle/init.md)

## Relationships

### Conforms To
- [ProductViewStyle](productviewstyle.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AutomaticProductViewStyle](automaticproductviewstyle.md)
- [struct RegularProductViewStyle](regularproductviewstyle.md)
  A style for a product view that uses a standard, platform-appropriate layout.
- [struct LargeProductViewStyle](largeproductviewstyle.md)
  A style for a product view that’s suitable for layouts where the in-app purchase content is prominent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/compactproductviewstyle)*