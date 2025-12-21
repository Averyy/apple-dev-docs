# autorecalculatesKeyViewLoop

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window automatically recalculates the key view loop when views are added.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var autorecalculatesKeyViewLoop: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the window automatically recalculates the key view loop when views are added; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). If [`autorecalculatesKeyViewLoop`](nswindow/autorecalculateskeyviewloop.md) is [`false`](https://developer.apple.com/documentation/Swift/false), the client code must update the key view loop manually or call [`recalculateKeyViewLoop()`](nswindow/recalculatekeyviewloop().md) to have the window recalculate it.

## See Also

- [func selectKeyView(preceding: NSView)](nswindow/selectkeyview(preceding:).md)
  Gives key view status to the view that precedes the given view.
- [func selectKeyView(following: NSView)](nswindow/selectkeyview(following:).md)
  Gives key view status to the view that follows the given view.
- [func selectPreviousKeyView(Any?)](nswindow/selectpreviouskeyview(_:).md)
  Searches for a candidate previous key view and, if it finds one, tries to make it the first responder.
- [func selectNextKeyView(Any?)](nswindow/selectnextkeyview(_:).md)
  Searches for a candidate next key view and, if it finds one, tries to make it the first responder.
- [var keyViewSelectionDirection: NSWindow.SelectionDirection](nswindow/keyviewselectiondirection.md)
  The direction the window is currently using to change the key view.
- [func recalculateKeyViewLoop()](nswindow/recalculatekeyviewloop.md)
  Marks the key view loop as “dirty” and in need of recalculation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/autorecalculateskeyviewloop)*