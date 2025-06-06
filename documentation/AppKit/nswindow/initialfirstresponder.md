# initialFirstResponder

**Framework**: AppKit  
**Kind**: property

The view that’s made first responder (also called the key view) the first time the window is placed onscreen.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var initialFirstResponder: NSView? { get set }
```

## See Also

- [var nextKeyView: NSView?](nsview/nextkeyview.md)
  The view object that follows the current view in the key view loop.
- [var firstResponder: NSResponder?](nswindow/firstresponder.md)
  The window’s first responder.
- [func makeFirstResponder(NSResponder?) -> Bool](nswindow/makefirstresponder(_:).md)
  Attempts to make a given responder the first responder for the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/initialfirstresponder)*