# selectPreviousKeyView(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Searches for a candidate previous key view and, if it finds one, tries to make it the first responder.

**Availability**:
- macOS

## Declaration

```swift
func selectPreviousKeyView(_ sender: Any?)
```

```objc
- (void) selectPreviousKeyView:(id) sender;
```

## Discussion

The candidate is one of the following (which this function searches for in this order):

- The current first responder’s previous valid key view, which the [`previousValidKeyView`](../nsview/previousvalidkeyview.md) method of `NSView` returns
- The [`initialFirstResponder`](./initialfirstresponder.md) designates as the window’s initial first responder if it returns [`true`](../../Swift/true.md) to an [`acceptsFirstResponder`](../nsresponder/acceptsfirstresponder.md) message
- Otherwise, the initial first responder’s previous valid key view, which may be `nil`

## Parameters

- `sender`: The message’s sender.

## See Also

### Managing the Key View Loop
- [func selectKeyView(preceding: NSView)](./selectkeyview%28preceding%29.md)
  Gives key view status to the view that precedes the given view.
- [func selectKeyView(following: NSView)](./selectkeyview%28following%29.md)
  Gives key view status to the view that follows the given view.
- [func selectNextKeyView(Any?)](./selectnextkeyview%28_%29.md)
  Searches for a candidate next key view and, if it finds one, tries to make it the first responder.
- [var keyViewSelectionDirection: NSWindow.SelectionDirection](./keyviewselectiondirection.md)
  The direction the window is currently using to change the key view.
- [var autorecalculatesKeyViewLoop: Bool](./autorecalculateskeyviewloop.md)
  A Boolean value that indicates whether the window automatically recalculates the key view loop when views are added.
- [func recalculateKeyViewLoop()](./recalculatekeyviewloop%28%29.md)
  Marks the key view loop as “dirty” and in need of recalculation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/selectpreviouskeyview(_:))*