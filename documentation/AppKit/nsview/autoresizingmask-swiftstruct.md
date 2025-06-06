# NSView.AutoresizingMask

**Framework**: AppKit  
**Kind**: struct

Constants that specify the autoresizing behaviors for views.

**Availability**:
- macOS ?+

## Declaration

```swift
struct AutoresizingMask
```

## Topics

### Getting the Autoresizing mask
- [static var none: NSView.AutoresizingMask](nsview/autoresizingmask-swift.struct/none.md)
  The view cannot be resized.
- [static var minXMargin: NSView.AutoresizingMask](nsview/autoresizingmask-swift.struct/minxmargin.md)
  The left margin between the view and its superview is flexible.
- [static var width: NSView.AutoresizingMask](nsview/autoresizingmask-swift.struct/width.md)
  The view’s width is flexible.
- [static var maxXMargin: NSView.AutoresizingMask](nsview/autoresizingmask-swift.struct/maxxmargin.md)
  The right margin between the view and its superview is flexible.
- [static var minYMargin: NSView.AutoresizingMask](nsview/autoresizingmask-swift.struct/minymargin.md)
  The bottom margin between the view and its superview is flexible.
- [static var height: NSView.AutoresizingMask](nsview/autoresizingmask-swift.struct/height.md)
  The view’s height is flexible.
- [static var maxYMargin: NSView.AutoresizingMask](nsview/autoresizingmask-swift.struct/maxymargin.md)
  The top margin between the view and its superview is flexible.
### Creating an Autoresizing Mask
- [init(rawValue: UInt)](nsview/autoresizingmask-swift.struct/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var autoresizesSubviews: Bool](nsview/autoresizessubviews.md)
  A Boolean value indicating whether the view applies the autoresizing behavior to its subviews when its frame size changes.
- [var autoresizingMask: NSView.AutoresizingMask](nsview/autoresizingmask-swift.property.md)
  The options that determine how the view is resized relative to its superview.
- [func resizeSubviews(withOldSize: NSSize)](nsview/resizesubviews(witholdsize:).md)
  Informs the view’s subviews that the view’s bounds rectangle size has changed.
- [func resize(withOldSuperviewSize: NSSize)](nsview/resize(witholdsuperviewsize:).md)
  Informs the view that the bounds size of its superview has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/autoresizingmask-swift.struct)*