# CompactProductViewStyle

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

A style for a product view that’s suitable for layouts with less available space, or for displaying more items in a small amount of space.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
@MainActor
@preconcurrency struct CompactProductViewStyle
```

## Topics

### Getting the compact product view style
- [static var compact: CompactProductViewStyle](./productviewstyle/compact.md)
  An product view style suitable for layouts where less space is available, or for displaying more items in a small amount of space.
### Creating the style
- [init()](./compactproductviewstyle/init%28%29.md)

## Relationships

### Conforms To
- [ProductViewStyle](./productviewstyle.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [struct AutomaticProductViewStyle](./automaticproductviewstyle.md)
- [struct RegularProductViewStyle](./regularproductviewstyle.md)
  A style for a product view that uses a standard, platform-appropriate layout.
- [struct LargeProductViewStyle](./largeproductviewstyle.md)
  A style for a product view that’s suitable for layouts where the Apple In-App Purchase content is prominent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/compactproductviewstyle)*