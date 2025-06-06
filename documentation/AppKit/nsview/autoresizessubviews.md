# autoresizesSubviews

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view applies the autoresizing behavior to its subviews when its frame size changes.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var autoresizesSubviews: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true) and the view’s frame changes, the view automatically calls the [`resizeSubviews(withOldSize:)`](nsview/resizesubviews(witholdsize:).md) method to facilitate the resizing of its subviews. When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), the view does not autoresize its subviews.

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var autoresizingMask: NSView.AutoresizingMask](nsview/autoresizingmask-swift.property.md)
  The options that determine how the view is resized relative to its superview.
- [NSView.AutoresizingMask](nsview/autoresizingmask-swift.struct.md)
  Constants that specify the autoresizing behaviors for views.
- [func resizeSubviews(withOldSize: NSSize)](nsview/resizesubviews(witholdsize:).md)
  Informs the view’s subviews that the view’s bounds rectangle size has changed.
- [func resize(withOldSuperviewSize: NSSize)](nsview/resize(witholdsuperviewsize:).md)
  Informs the view that the bounds size of its superview has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/autoresizessubviews)*