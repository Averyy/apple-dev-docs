# resize(withOldSuperviewSize:)

**Framework**: AppKit  
**Kind**: method

Informs the view that the bounds size of its superview has changed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func resize(withOldSuperviewSize oldSize: NSSize)
```

#### Discussion

This method is normally invoked automatically from [`resizeSubviews(withOldSize:)`](nsview/resizesubviews(witholdsize:).md).

The default implementation resizes the view according to the autoresizing options specified by the [`autoresizingMask`](nsview/autoresizingmask-swift.property.md) property. You shouldn’t invoke this method directly, but you can override it to define a specific resizing behavior.

If you override this method and call `super` as part of your implementation, you should be sure to call `super` before making changes to the receiving view’s frame yourself.

## Parameters

- `oldSize`: The previous size of the superview’s bounds rectangle.

## See Also

- [var autoresizesSubviews: Bool](nsview/autoresizessubviews.md)
  A Boolean value indicating whether the view applies the autoresizing behavior to its subviews when its frame size changes.
- [var autoresizingMask: NSView.AutoresizingMask](nsview/autoresizingmask-swift.property.md)
  The options that determine how the view is resized relative to its superview.
- [NSView.AutoresizingMask](nsview/autoresizingmask-swift.struct.md)
  Constants that specify the autoresizing behaviors for views.
- [func resizeSubviews(withOldSize: NSSize)](nsview/resizesubviews(witholdsize:).md)
  Informs the view’s subviews that the view’s bounds rectangle size has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/resize(witholdsuperviewsize:))*