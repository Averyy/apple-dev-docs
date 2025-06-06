# reflectScrolledClipView(_:)

**Framework**: AppKit  
**Kind**: method

Adjusts the receiver’s scrollers to reflect the size and positioning of its content view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func reflectScrolledClipView(_ cView: NSClipView)
```

#### Discussion

This method is invoked automatically during scrolling and when an `NSClipView` object’s relationship to its document view changes; you should rarely need to invoke it yourself, but may wish to override it for custom updating or other behavior. If you override this method, be sure to call the superclass implementation. If you do not, other controls (such as the current scrollers) may not be updated properly.

## Parameters

- `cView`: The clip view being adjusted to. If   is any view object other than the receiver’s content view, the method does nothing.

## See Also

- [var documentView: NSView?](nsscrollview/documentview.md)
  The view the scroll view scrolls within its content view.
- [var contentView: NSClipView](nsscrollview/contentview.md)
  The scroll view’s content view, the view that clips the document view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/reflectscrolledclipview(_:))*