# preferredContentSize

**Framework**: SwiftUI  
**Kind**: property

The hosting controller creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting controller’s `preferredContentSize`.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static let preferredContentSize: NSHostingSizingOptions
```

#### Discussion

The constraints reflect the size that fits a proposal of `.unspecified`.

> **Note**: This option has no effect when used with an `NSHostingView` directly.

This option has no effect when used with an `NSHostingView` directly.

## See Also

- [static let intrinsicContentSize: NSHostingSizingOptions](nshostingsizingoptions/intrinsiccontentsize.md)
  The hosting view creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting view’s `intrinsicContentSize`.
- [static let maxSize: NSHostingSizingOptions](nshostingsizingoptions/maxsize.md)
  The hosting view creates and updates constraints that represent its content’s maximum size.
- [static let minSize: NSHostingSizingOptions](nshostingsizingoptions/minsize.md)
  The hosting view creates and updates constraints that represent its content’s minimum size.
- [static let standardBounds: NSHostingSizingOptions](nshostingsizingoptions/standardbounds.md)
  The hosting view creates constraints for its minimum, ideal, and maximum sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingsizingoptions/preferredcontentsize)*