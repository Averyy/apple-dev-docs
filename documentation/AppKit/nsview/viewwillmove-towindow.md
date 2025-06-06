# viewWillMove(toWindow:)

**Framework**: AppKit  
**Kind**: method

Informs the view that it’s being added to the view hierarchy of the specified window object (which may be `nil`).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func viewWillMove(toWindow newWindow: NSWindow?)
```

#### Discussion

AppKit calls this method when the window of a view changes. It also calls it in cases where a view stays in the same window but its position in its view hierarchy changes. The view that moved also calls this method on all of its subviews, giving each of them a chance to respond to the change.

Subclasses can override this method to perform whatever actions are necessary. For example, when a window is deallocated, you can use this method to remove notification observers and bindings associated with the view.

When a window is deallocated, AppKit calls this method for each view in the window, passing `nil` for the `newWindow` parameter. AppKit does not necessarily call this method when closing a window, though. Closing a window usually just hides the window. Closed windows are deallocated only if their [`isReleasedWhenClosed`](nswindow/isreleasedwhenclosed.md) method returns [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `newWindow`: The window object that will be at the root of the view’s new view hierarchy. If the view is being removed from a window and there is no new window, this parameter is  .

## See Also

- [func didAddSubview(NSView)](nsview/didaddsubview(_:).md)
  Overridden by subclasses to perform additional actions when subviews are added to the view.
- [func viewDidMoveToSuperview()](nsview/viewdidmovetosuperview.md)
  Informs the view that its superview has changed (possibly to `nil`).
- [func viewDidMoveToWindow()](nsview/viewdidmovetowindow.md)
  Informs the view that it has been added to a new view hierarchy.
- [func viewWillMove(toSuperview: NSView?)](nsview/viewwillmove(tosuperview:).md)
  Informs the view that its superview is about to change to the specified superview (which may be `nil`).
- [func willRemoveSubview(NSView)](nsview/willremovesubview(_:).md)
  Overridden by subclasses to perform additional actions before subviews are removed from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/viewwillmove(towindow:))*