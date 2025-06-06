# autoresizingMask

**Framework**: AppKit  
**Kind**: property

The options that determine how the view is resized relative to its superview.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var autoresizingMask: NSView.AutoresizingMask { get set }
```

#### Discussion

The value of this property is an integer bit mask specified by combining the options described in [`NSView.AutoresizingMask`](nsview/autoresizingmask-swift.struct.md). This mask is used by the [`resize(withOldSuperviewSize:)`](nsview/resize(witholdsuperviewsize:).md) method when the view needs to be resized.

If the autoresizing mask is set to `NSViewNotSizable` (that is, if none of the options are set), the view does not resize at all. When more than one option along an axis is set, the [`resize(withOldSuperviewSize:)`](nsview/resize(witholdsuperviewsize:).md) method distributes the size difference as evenly as possible among the flexible portions. For example, if `NSViewWidthSizable` and `NSViewMaxXMargin` are set and the superview’s width has increased by `10.0` points, the view’s frame and right margin are each widened by `5.0` points.

## See Also

- [var autoresizesSubviews: Bool](nsview/autoresizessubviews.md)
  A Boolean value indicating whether the view applies the autoresizing behavior to its subviews when its frame size changes.
- [NSView.AutoresizingMask](nsview/autoresizingmask-swift.struct.md)
  Constants that specify the autoresizing behaviors for views.
- [func resizeSubviews(withOldSize: NSSize)](nsview/resizesubviews(witholdsize:).md)
  Informs the view’s subviews that the view’s bounds rectangle size has changed.
- [func resize(withOldSuperviewSize: NSSize)](nsview/resize(witholdsuperviewsize:).md)
  Informs the view that the bounds size of its superview has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/autoresizingmask-swift.property)*