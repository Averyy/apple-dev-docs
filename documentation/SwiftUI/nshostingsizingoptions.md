# NSHostingSizingOptions

**Framework**: SwiftUI  
**Kind**: struct

Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.

**Availability**:
- macOS 13.0+

## Declaration

```swift
struct NSHostingSizingOptions
```

## Topics

### Geting sizing options
- [static let intrinsicContentSize: NSHostingSizingOptions](nshostingsizingoptions/intrinsiccontentsize.md)
  The hosting view creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting view’s `intrinsicContentSize`.
- [static let maxSize: NSHostingSizingOptions](nshostingsizingoptions/maxsize.md)
  The hosting view creates and updates constraints that represent its content’s maximum size.
- [static let minSize: NSHostingSizingOptions](nshostingsizingoptions/minsize.md)
  The hosting view creates and updates constraints that represent its content’s minimum size.
- [static let preferredContentSize: NSHostingSizingOptions](nshostingsizingoptions/preferredcontentsize.md)
  The hosting controller creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting controller’s `preferredContentSize`.
- [static let standardBounds: NSHostingSizingOptions](nshostingsizingoptions/standardbounds.md)
  The hosting view creates constraints for its minimum, ideal, and maximum sizes.
### Creating a sizing option
- [init(rawValue: Int)](nshostingsizingoptions/init(rawvalue:).md)
  Creates a new options from a raw value.
- [let rawValue: Int](nshostingsizingoptions/rawvalue.md)
  The raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Unifying your app’s animations](unifying-your-app-s-animations.md)
  Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [class NSHostingController](nshostingcontroller.md)
  An AppKit view controller that hosts SwiftUI view hierarchy.
- [class NSHostingView](nshostingview.md)
  An AppKit view that hosts a SwiftUI view hierarchy.
- [class NSHostingMenu](nshostingmenu.md)
  An AppKit menu with menu items that are defined by a SwiftUI View.
- [struct NSHostingSceneBridgingOptions](nshostingscenebridgingoptions.md)
  Options for how hosting views and controllers manage aspects of the associated window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingsizingoptions)*