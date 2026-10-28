# autoresizesSubviews

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view applies the autoresizing behavior to its subviews when its frame size changes.

**Availability**:
- macOS

## Declaration

```swift
var autoresizesSubviews: Bool { get set }
```

```objc
@property BOOL autoresizesSubviews;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md) and the view’s frame changes, the view automatically calls the [`resizeSubviews(withOldSize:)`](./resizesubviews%28witholdsize%29.md) method to facilitate the resizing of its subviews. When the value of this property is [`false`](../../Swift/false.md), the view does not autoresize its subviews.

The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Resizing Subviews
- [var autoresizingMask: NSView.AutoresizingMask](./autoresizingmask-swift.property.md)
  The options that determine how the view is resized relative to its superview.
- [NSView.AutoresizingMask](./autoresizingmask-swift.struct.md)
  Constants that specify the autoresizing behaviors for views.
- [func resizeSubviews(withOldSize: NSSize)](./resizesubviews%28witholdsize%29.md)
  Informs the view’s subviews that the view’s bounds rectangle size has changed.
- [func resize(withOldSuperviewSize: NSSize)](./resize%28witholdsuperviewsize%29.md)
  Informs the view that the bounds size of its superview has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/autoresizessubviews)*