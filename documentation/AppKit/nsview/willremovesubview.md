# willRemoveSubview(_:)

**Framework**: AppKit  
**Kind**: method

Overridden by subclasses to perform additional actions before subviews are removed from the view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func willRemoveSubview(_ subview: NSView)
```

#### Discussion

This method is invoked when `subview` receives a [`removeFromSuperview()`](nsview/removefromsuperview().md) message or `subview` is removed from the view due to it being added to another view with [`addSubview(_:)`](nsview/addsubview(_:).md).

## Parameters

- `subview`: The subview that will be removed.

## See Also

- [func didAddSubview(NSView)](nsview/didaddsubview(_:).md)
  Overridden by subclasses to perform additional actions when subviews are added to the view.
- [func viewDidMoveToSuperview()](nsview/viewdidmovetosuperview.md)
  Informs the view that its superview has changed (possibly to `nil`).
- [func viewDidMoveToWindow()](nsview/viewdidmovetowindow.md)
  Informs the view that it has been added to a new view hierarchy.
- [func viewWillMove(toSuperview: NSView?)](nsview/viewwillmove(tosuperview:).md)
  Informs the view that its superview is about to change to the specified superview (which may be `nil`).
- [func viewWillMove(toWindow: NSWindow?)](nsview/viewwillmove(towindow:).md)
  Informs the view that it’s being added to the view hierarchy of the specified window object (which may be `nil`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/willremovesubview(_:))*