# selectNextKeyView(_:)

**Framework**: AppKit  
**Kind**: method

Searches for a candidate next key view and, if it finds one, tries to make it the first responder.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectNextKeyView(_ sender: Any?)
```

#### Discussion

The candidate is one of the following (which this function searches for in this order):

- The current first responder’s next valid key view, which the [`nextValidKeyView`](nsview/nextvalidkeyview.md) method of `NSView` returns
- The object [`initialFirstResponder`](nswindow/initialfirstresponder.md) designates as the window’s initial first responder if it returns [`true`](https://developer.apple.com/documentation/swift/true) to an [`acceptsFirstResponder`](nsresponder/acceptsfirstresponder.md) message
- Otherwise, the initial first responder’s next valid key view, which may be `nil`

## Parameters

- `sender`: The message’s sender.

## See Also

- [func selectKeyView(preceding: NSView)](nswindow/selectkeyview(preceding:).md)
  Gives key view status to the view that precedes the given view.
- [func selectKeyView(following: NSView)](nswindow/selectkeyview(following:).md)
  Gives key view status to the view that follows the given view.
- [func selectPreviousKeyView(Any?)](nswindow/selectpreviouskeyview(_:).md)
  Searches for a candidate previous key view and, if it finds one, tries to make it the first responder.
- [var keyViewSelectionDirection: NSWindow.SelectionDirection](nswindow/keyviewselectiondirection.md)
  The direction the window is currently using to change the key view.
- [var autorecalculatesKeyViewLoop: Bool](nswindow/autorecalculateskeyviewloop.md)
  A Boolean value that indicates whether the window automatically recalculates the key view loop when views are added.
- [func recalculateKeyViewLoop()](nswindow/recalculatekeyviewloop.md)
  Marks the key view loop as “dirty” and in need of recalculation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/selectnextkeyview(_:))*