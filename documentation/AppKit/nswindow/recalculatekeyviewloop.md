# recalculateKeyViewLoop()

**Framework**: AppKit  
**Kind**: method

Marks the key view loop as “dirty” and in need of recalculation.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func recalculateKeyViewLoop()
```

#### Discussion

The key view loop is recalculated the next time someone requests the next or previous key view of the window. The recalculated loop is based on the geometric order of the views in the window.

If you don’t want to maintain the key view loop of your window manually, you can use this method to do it for you. When it’s first loaded, `NSWindow` calls this method automatically if your window doesn’t have a key view loop already established. If you add or remove views later, you can call this method manually to update the window’s key view loop. You can also set the [`autorecalculatesKeyViewLoop`](nswindow/autorecalculateskeyviewloop.md) property to have the window recalculate the loop automatically.

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
- [var autorecalculatesKeyViewLoop: Bool](nswindow/autorecalculateskeyviewloop.md)
  A Boolean value that indicates whether the window automatically recalculates the key view loop when views are added.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/recalculatekeyviewloop())*