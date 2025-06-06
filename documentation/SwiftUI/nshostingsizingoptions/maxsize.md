# maxSize

**Framework**: SwiftUI  
**Kind**: property

The hosting view creates and updates constraints that represent its content’s maximum size.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static let maxSize: NSHostingSizingOptions
```

#### Discussion

The constraints reflect the size that fits a proposal of `width: infinity, height: infinity`.

## See Also

- [static let intrinsicContentSize: NSHostingSizingOptions](nshostingsizingoptions/intrinsiccontentsize.md)
  The hosting view creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting view’s `intrinsicContentSize`.
- [static let minSize: NSHostingSizingOptions](nshostingsizingoptions/minsize.md)
  The hosting view creates and updates constraints that represent its content’s minimum size.
- [static let preferredContentSize: NSHostingSizingOptions](nshostingsizingoptions/preferredcontentsize.md)
  The hosting controller creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting controller’s `preferredContentSize`.
- [static let standardBounds: NSHostingSizingOptions](nshostingsizingoptions/standardbounds.md)
  The hosting view creates constraints for its minimum, ideal, and maximum sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingsizingoptions/maxsize)*