# regular

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

A product view style that uses a standard, platform-appropriate layout.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency static var regular: RegularProductViewStyle { get }
```

Available when `Self` is `RegularProductViewStyle`.

## See Also

### Getting built-in product view styles
- [static var automatic: AutomaticProductViewStyle](./automatic.md)
- [static var compact: CompactProductViewStyle](./compact.md)
  An product view style suitable for layouts where less space is available, or for displaying more items in a small amount of space.
- [static var large: LargeProductViewStyle](./large.md)
  A product view style suitable for layouts where the Apple In-App Purchase content is prominent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/productviewstyle/regular)*