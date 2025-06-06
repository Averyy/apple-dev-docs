# contentView

**Framework**: AppKit  
**Kind**: property

The window’s content view, the highest accessible view object in the window’s view hierarchy.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var contentView: NSView? { get set }
```

#### Discussion

The window retains the new content view and owns it thereafter. The `view` object is resized to fit precisely within the content area of the window. You can modify the content view’s coordinate system through its bounds rectangle, but you can’t alter its frame rectangle (its size or location) directly.

Setting this property releases the old content view. If you plan to reuse it, be sure to retain it before changing the property value and to release it as appropriate when adding it to another `NSWindow` or [`NSView`](nsview.md) object.

## See Also

- [func setContentSize(NSSize)](nswindow/setcontentsize(_:).md)
  Sets the size of the window’s content view to a given size, which is expressed in the window’s base coordinate system.
- [var contentViewController: NSViewController?](nswindow/contentviewcontroller.md)
  The main content view controller for the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentview)*