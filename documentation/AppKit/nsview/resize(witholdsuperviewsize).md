# resize(withOldSuperviewSize:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the view that the bounds size of its superview has changed.

**Availability**:
- macOS

## Declaration

```swift
func resize(withOldSuperviewSize oldSize: NSSize)
```

```objc
- (void) resizeWithOldSuperviewSize:(NSSize) oldSize;
```

#### Discussion

This method is normally invoked automatically from [`resizeSubviews(withOldSize:)`](./resizesubviews%28witholdsize%29.md).

The default implementation resizes the view according to the autoresizing options specified by the [`autoresizingMask`](./autoresizingmask-swift.property.md) property. You shouldn’t invoke this method directly, but you can override it to define a specific resizing behavior.

If you override this method and call `super` as part of your implementation, you should be sure to call `super` before making changes to the receiving view’s frame yourself.

## Parameters

- `oldSize`: The previous size of the superview’s bounds rectangle.

## See Also

### Resizing Subviews
- [var autoresizesSubviews: Bool](./autoresizessubviews.md)
  A Boolean value indicating whether the view applies the autoresizing behavior to its subviews when its frame size changes.
- [var autoresizingMask: NSView.AutoresizingMask](./autoresizingmask-swift.property.md)
  The options that determine how the view is resized relative to its superview.
- [NSView.AutoresizingMask](./autoresizingmask-swift.struct.md)
  Constants that specify the autoresizing behaviors for views.
- [func resizeSubviews(withOldSize: NSSize)](./resizesubviews%28witholdsize%29.md)
  Informs the view’s subviews that the view’s bounds rectangle size has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/resize(witholdsuperviewsize:))*