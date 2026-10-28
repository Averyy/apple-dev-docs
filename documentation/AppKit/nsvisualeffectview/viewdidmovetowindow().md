# viewDidMoveToWindow()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies the view that it moved to a new window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func viewDidMoveToWindow()
```

```objc
- (void) viewDidMoveToWindow;
```

## Discussion

When subclassing, you can override this method and use it to perform any tasks associated with the change. You must call `super` at some point during your implementation.

## See Also

### Handling Moves to a Different Window
- [func viewWillMove(toWindow: NSWindow?)](./viewwillmove%28towindow%29.md)
  Notifies the view immediately before it moves to a new window (which may be `nil`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsvisualeffectview/viewdidmovetowindow())*