# didAddSubview(_:)

**Framework**: AppKit  
**Kind**: method

Overridden by subclasses to perform additional actions when subviews are added to the view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func didAddSubview(_ subview: NSView)
```

#### Discussion

This method is invoked by [`addSubview(_:)`](nsview/addsubview(_:).md).

## Parameters

- `subview`: The view that was added as a subview.

## See Also

- [func viewDidMoveToSuperview()](nsview/viewdidmovetosuperview.md)
  Informs the view that its superview has changed (possibly to `nil`).
- [func viewDidMoveToWindow()](nsview/viewdidmovetowindow.md)
  Informs the view that it has been added to a new view hierarchy.
- [func viewWillMove(toSuperview: NSView?)](nsview/viewwillmove(tosuperview:).md)
  Informs the view that its superview is about to change to the specified superview (which may be `nil`).
- [func viewWillMove(toWindow: NSWindow?)](nsview/viewwillmove(towindow:).md)
  Informs the view that it’s being added to the view hierarchy of the specified window object (which may be `nil`).
- [func willRemoveSubview(NSView)](nsview/willremovesubview(_:).md)
  Overridden by subclasses to perform additional actions before subviews are removed from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/didaddsubview(_:))*