# selectKeyView(preceding:)

**Framework**: AppKit  
**Kind**: method

Gives key view status to the view that precedes the given view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectKeyView(preceding view: NSView)
```

#### Discussion

Sends the [`previousValidKeyView`](nsview/previousvalidkeyview.md) message to `view` and, if that message returns an `NSView` object, invokes [`makeFirstResponder(_:)`](nswindow/makefirstresponder(_:).md) with the returned object.

## Parameters

- `view`: The view whose preceding view in the key view loop to seek.

## See Also

- [func selectKeyView(following: NSView)](nswindow/selectkeyview(following:).md)
  Gives key view status to the view that follows the given view.
- [func selectPreviousKeyView(Any?)](nswindow/selectpreviouskeyview(_:).md)
  Searches for a candidate previous key view and, if it finds one, tries to make it the first responder.
- [func selectNextKeyView(Any?)](nswindow/selectnextkeyview(_:).md)
  Searches for a candidate next key view and, if it finds one, tries to make it the first responder.
- [var keyViewSelectionDirection: NSWindow.SelectionDirection](nswindow/keyviewselectiondirection.md)
  The direction the window is currently using to change the key view.
- [var autorecalculatesKeyViewLoop: Bool](nswindow/autorecalculateskeyviewloop.md)
  A Boolean value that indicates whether the window automatically recalculates the key view loop when views are added.
- [func recalculateKeyViewLoop()](nswindow/recalculatekeyviewloop.md)
  Marks the key view loop as “dirty” and in need of recalculation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/selectkeyview(preceding:))*