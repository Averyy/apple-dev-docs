# maxSize

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The hosting view creates and updates constraints that represent its content’s maximum size.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static let maxSize: NSHostingSizingOptions
```

## Discussion

The constraints reflect the size that fits a proposal of `width: infinity, height: infinity`.

## See Also

### Geting sizing options
- [static let intrinsicContentSize: NSHostingSizingOptions](./intrinsiccontentsize.md)
  The hosting view creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting view’s `intrinsicContentSize`.
- [static let minSize: NSHostingSizingOptions](./minsize.md)
  The hosting view creates and updates constraints that represent its content’s minimum size.
- [static let preferredContentSize: NSHostingSizingOptions](./preferredcontentsize.md)
  The hosting controller creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting controller’s `preferredContentSize`.
- [static let standardBounds: NSHostingSizingOptions](./standardbounds.md)
  The hosting view creates constraints for its minimum, ideal, and maximum sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingsizingoptions/maxsize)*