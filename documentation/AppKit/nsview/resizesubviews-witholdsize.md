# resizeSubviews(withOldSize:)

**Framework**: AppKit  
**Kind**: method

Informs the view’s subviews that the view’s bounds rectangle size has changed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func resizeSubviews(withOldSize oldSize: NSSize)
```

#### Discussion

If the view is configured to autoresize its subviews, this method is automatically invoked by any method that changes the view’s frame size.

The default implementation sends [`resize(withOldSuperviewSize:)`](nsview/resize(witholdsuperviewsize:).md) to the view’s subviews with `oldBoundsSize` as the argument. You shouldn’t invoke this method directly, but you can override it to define a specific resizing behavior.

## Parameters

- `oldSize`: The previous size of the view’s bounds rectangle.

## See Also

- [var autoresizesSubviews: Bool](nsview/autoresizessubviews.md)
  A Boolean value indicating whether the view applies the autoresizing behavior to its subviews when its frame size changes.
- [var autoresizingMask: NSView.AutoresizingMask](nsview/autoresizingmask-swift.property.md)
  The options that determine how the view is resized relative to its superview.
- [NSView.AutoresizingMask](nsview/autoresizingmask-swift.struct.md)
  Constants that specify the autoresizing behaviors for views.
- [func resize(withOldSuperviewSize: NSSize)](nsview/resize(witholdsuperviewsize:).md)
  Informs the view that the bounds size of its superview has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/resizesubviews(witholdsize:))*