# viewDidMoveToWindow()

**Framework**: AppKit  
**Kind**: method

Notifies the view that it moved to a new window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func viewDidMoveToWindow()
```

#### Discussion

When subclassing, you can override this method and use it to perform any tasks associated with the change. You must call `super` at some point during your implementation.

## See Also

- [func viewWillMove(toWindow: NSWindow?)](nsvisualeffectview/viewwillmove(towindow:).md)
  Notifies the view immediately before it moves to a new window (which may be `nil`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsvisualeffectview/viewdidmovetowindow())*