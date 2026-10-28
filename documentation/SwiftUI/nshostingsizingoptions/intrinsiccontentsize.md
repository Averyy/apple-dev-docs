# intrinsicContentSize

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The hosting view creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting view’s `intrinsicContentSize`.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static let intrinsicContentSize: NSHostingSizingOptions
```

## Discussion

The constraints reflect the size that fits a proposal of `.unspecified`.

## See Also

### Geting sizing options
- [static let maxSize: NSHostingSizingOptions](./maxsize.md)
  The hosting view creates and updates constraints that represent its content’s maximum size.
- [static let minSize: NSHostingSizingOptions](./minsize.md)
  The hosting view creates and updates constraints that represent its content’s minimum size.
- [static let preferredContentSize: NSHostingSizingOptions](./preferredcontentsize.md)
  The hosting controller creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting controller’s `preferredContentSize`.
- [static let standardBounds: NSHostingSizingOptions](./standardbounds.md)
  The hosting view creates constraints for its minimum, ideal, and maximum sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingsizingoptions/intrinsiccontentsize)*