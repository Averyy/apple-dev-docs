# contentView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The window’s content view, the highest accessible view object in the window’s view hierarchy.

**Availability**:
- macOS

## Declaration

```swift
var contentView: NSView? { get set }
```

```objc
@property (strong, nullable) NSView * contentView;
```

#### Discussion

The window retains the new content view and owns it thereafter. The `view` object is resized to fit precisely within the content area of the window. You can modify the content view’s coordinate system through its bounds rectangle, but you can’t alter its frame rectangle (its size or location) directly.

Setting this property releases the old content view. If you plan to reuse it, be sure to retain it before changing the property value and to release it as appropriate when adding it to another `NSWindow` or [`NSView`](../nsview.md) object.

## See Also

### Related Documentation
- [func setContentSize(NSSize)](./setcontentsize%28_%29.md)
  Sets the size of the window’s content view to a given size, which is expressed in the window’s base coordinate system.
### Configuring the Window’s Content
- [var contentViewController: NSViewController?](./contentviewcontroller.md)
  The main content view controller for the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentview)*