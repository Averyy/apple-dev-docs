# documentView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view the scroll view scrolls within its content view.

**Availability**:
- macOS

## Declaration

```swift
var documentView: NSView? { get set }
```

```objc
@property (strong, nullable) NSView * documentView;
```

## See Also

### Related Documentation
- [var documentView: NSView?](../nsclipview/documentview.md)
  The clip view’s document view.
### Managing the Views
- [var contentView: NSClipView](./contentview.md)
  The scroll view’s content view, the view that clips the document view.
- [func addFloatingSubview(NSView, for: NSEvent.GestureAxis)](./addfloatingsubview%28_,for%29.md)
  Adds a floating subview to the document view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/documentview)*