# didAddSubview(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Overridden by subclasses to perform additional actions when subviews are added to the view.

**Availability**:
- macOS

## Declaration

```swift
func didAddSubview(_ subview: NSView)
```

```objc
- (void) didAddSubview:(NSView *) subview;
```

## Discussion

This method is invoked by [`addSubview(_:)`](./addsubview%28_%29.md).

## Parameters

- `subview`: The view that was added as a subview.

## See Also

### Responding to View-Related Notifications
- [func viewDidMoveToSuperview()](./viewdidmovetosuperview%28%29.md)
  Informs the view that its superview has changed (possibly to `nil`).
- [func viewDidMoveToWindow()](./viewdidmovetowindow%28%29.md)
  Informs the view that it has been added to a new view hierarchy.
- [func viewWillMove(toSuperview: NSView?)](./viewwillmove%28tosuperview%29.md)
  Informs the view that its superview is about to change to the specified superview (which may be `nil`).
- [func viewWillMove(toWindow: NSWindow?)](./viewwillmove%28towindow%29.md)
  Informs the view that it’s being added to the view hierarchy of the specified window object (which may be `nil`).
- [func willRemoveSubview(NSView)](./willremovesubview%28_%29.md)
  Overridden by subclasses to perform additional actions before subviews are removed from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/didaddsubview(_:))*