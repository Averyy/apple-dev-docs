# viewDidMoveToSuperview()

**Framework**: AppKit  
**Kind**: method

Informs the view that its superview has changed (possibly to `nil`).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func viewDidMoveToSuperview()
```

#### Discussion

The default implementation does nothing; subclasses can override this method to perform whatever actions are necessary.

## See Also

- [func didAddSubview(NSView)](nsview/didaddsubview(_:).md)
  Overridden by subclasses to perform additional actions when subviews are added to the view.
- [func viewDidMoveToWindow()](nsview/viewdidmovetowindow.md)
  Informs the view that it has been added to a new view hierarchy.
- [func viewWillMove(toSuperview: NSView?)](nsview/viewwillmove(tosuperview:).md)
  Informs the view that its superview is about to change to the specified superview (which may be `nil`).
- [func viewWillMove(toWindow: NSWindow?)](nsview/viewwillmove(towindow:).md)
  Informs the view that it’s being added to the view hierarchy of the specified window object (which may be `nil`).
- [func willRemoveSubview(NSView)](nsview/willremovesubview(_:).md)
  Overridden by subclasses to perform additional actions before subviews are removed from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/viewdidmovetosuperview())*