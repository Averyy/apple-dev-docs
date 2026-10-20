# parentWindow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s parent window.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
unowned(unsafe) var parentWindow: NSWindow? { get set }
```

```objc
@property (assign, nullable) NSWindow * parentWindow;
```

#### Discussion

Changes in a drawer’s parent window do not take place while the drawer is onscreen; they are delayed until the drawer next closes.

## See Also

### Managing Drawer Views
- [var contentView: NSView?](./contentview.md)
  The receiver’s content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/parentwindow)*