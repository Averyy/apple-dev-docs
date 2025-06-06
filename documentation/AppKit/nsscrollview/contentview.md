# contentView

**Framework**: AppKit  
**Kind**: property

The scroll view’s content view, the view that clips the document view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var contentView: NSClipView { get set }
```

#### Discussion

Setting the value of this property to an `NSClipView` that has a document view also sets the scroll view’s document view to be the document view of that `NSClipView`. The original content view retains its document view.

## See Also

- [var documentView: NSView?](nsscrollview/documentview.md)
  The view the scroll view scrolls within its content view.
- [func addFloatingSubview(NSView, for: NSEvent.GestureAxis)](nsscrollview/addfloatingsubview(_:for:).md)
  Adds a floating subview to the document view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/contentview)*