# willRemoveSubview(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Overridden by subclasses to perform additional actions before subviews are removed from the view.

**Availability**:
- macOS

## Declaration

```swift
func willRemoveSubview(_ subview: NSView)
```

```objc
- (void) willRemoveSubview:(NSView *) subview;
```

#### Discussion

This method is invoked when `subview` receives a [`removeFromSuperview()`](./removefromsuperview%28%29.md) message or `subview` is removed from the view due to it being added to another view with [`addSubview(_:)`](./addsubview%28_%29.md).

## Parameters

- `subview`: The subview that will be removed.

## See Also

### Responding to View-Related Notifications
- [func didAddSubview(NSView)](./didaddsubview%28_%29.md)
  Overridden by subclasses to perform additional actions when subviews are added to the view.
- [func viewDidMoveToSuperview()](./viewdidmovetosuperview%28%29.md)
  Informs the view that its superview has changed (possibly to `nil`).
- [func viewDidMoveToWindow()](./viewdidmovetowindow%28%29.md)
  Informs the view that it has been added to a new view hierarchy.
- [func viewWillMove(toSuperview: NSView?)](./viewwillmove%28tosuperview%29.md)
  Informs the view that its superview is about to change to the specified superview (which may be `nil`).
- [func viewWillMove(toWindow: NSWindow?)](./viewwillmove%28towindow%29.md)
  Informs the view that it’s being added to the view hierarchy of the specified window object (which may be `nil`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/willremovesubview(_:))*