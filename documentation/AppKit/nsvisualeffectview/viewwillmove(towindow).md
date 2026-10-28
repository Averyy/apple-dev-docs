# viewWillMove(toWindow:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies the view immediately before it moves to a new window (which may be `nil`).

**Availability**:
- macOS 10.10+

## Declaration

```swift
func viewWillMove(toWindow newWindow: NSWindow?)
```

```objc
- (void) viewWillMoveToWindow:(NSWindow *) newWindow;
```

## Discussion

When subclassing, you can override this method and use it to perform any tasks associated with the change. You must call `super` at some point during your implementation.

## Parameters

- `newWindow`: The window object that will be at the root of the view’s new view hierarchy. If the view is being removed from a window and there isn’t a new window, this parameter is `nil`.

## See Also

### Handling Moves to a Different Window
- [func viewDidMoveToWindow()](./viewdidmovetowindow%28%29.md)
  Notifies the view that it moved to a new window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsvisualeffectview/viewwillmove(towindow:))*