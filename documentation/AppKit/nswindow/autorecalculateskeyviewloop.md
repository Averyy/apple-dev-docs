# autorecalculatesKeyViewLoop

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window automatically recalculates the key view loop when views are added.

**Availability**:
- macOS

## Declaration

```swift
var autorecalculatesKeyViewLoop: Bool { get set }
```

```objc
@property BOOL autorecalculatesKeyViewLoop;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the window automatically recalculates the key view loop when views are added; otherwise, [`false`](../../Swift/false.md). If [`autorecalculatesKeyViewLoop`](./autorecalculateskeyviewloop.md) is [`false`](../../Swift/false.md), the client code must update the key view loop manually or call [`recalculateKeyViewLoop()`](./recalculatekeyviewloop%28%29.md) to have the window recalculate it.

## See Also

### Managing the Key View Loop
- [func selectKeyView(preceding: NSView)](./selectkeyview%28preceding%29.md)
  Gives key view status to the view that precedes the given view.
- [func selectKeyView(following: NSView)](./selectkeyview%28following%29.md)
  Gives key view status to the view that follows the given view.
- [func selectPreviousKeyView(Any?)](./selectpreviouskeyview%28_%29.md)
  Searches for a candidate previous key view and, if it finds one, tries to make it the first responder.
- [func selectNextKeyView(Any?)](./selectnextkeyview%28_%29.md)
  Searches for a candidate next key view and, if it finds one, tries to make it the first responder.
- [var keyViewSelectionDirection: NSWindow.SelectionDirection](./keyviewselectiondirection.md)
  The direction the window is currently using to change the key view.
- [func recalculateKeyViewLoop()](./recalculatekeyviewloop%28%29.md)
  Marks the key view loop as “dirty” and in need of recalculation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/autorecalculateskeyviewloop)*