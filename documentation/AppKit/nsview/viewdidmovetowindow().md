# viewDidMoveToWindow()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the view that it has been added to a new view hierarchy.

**Availability**:
- macOS

## Declaration

```swift
func viewDidMoveToWindow()
```

```objc
- (void) viewDidMoveToWindow;
```

#### Discussion

The default implementation does nothing; subclasses can override this method to perform whatever actions are necessary.

If the view’s [`window`](./window.md) property is `nil`, that result signifies that the view was removed from its window and does not currently reside in any window.

## See Also

### Responding to View-Related Notifications
- [func didAddSubview(NSView)](./didaddsubview%28_%29.md)
  Overridden by subclasses to perform additional actions when subviews are added to the view.
- [func viewDidMoveToSuperview()](./viewdidmovetosuperview%28%29.md)
  Informs the view that its superview has changed (possibly to `nil`).
- [func viewWillMove(toSuperview: NSView?)](./viewwillmove%28tosuperview%29.md)
  Informs the view that its superview is about to change to the specified superview (which may be `nil`).
- [func viewWillMove(toWindow: NSWindow?)](./viewwillmove%28towindow%29.md)
  Informs the view that it’s being added to the view hierarchy of the specified window object (which may be `nil`).
- [func willRemoveSubview(NSView)](./willremovesubview%28_%29.md)
  Overridden by subclasses to perform additional actions before subviews are removed from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/viewdidmovetowindow())*