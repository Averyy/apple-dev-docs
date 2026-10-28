# selectKeyView(preceding:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Gives key view status to the view that precedes the given view.

**Availability**:
- macOS

## Declaration

```swift
func selectKeyView(preceding view: NSView)
```

```objc
- (void) selectKeyViewPrecedingView:(NSView *) view;
```

## Discussion

Sends the [`previousValidKeyView`](../nsview/previousvalidkeyview.md) message to `view` and, if that message returns an `NSView` object, invokes [`makeFirstResponder(_:)`](./makefirstresponder%28_%29.md) with the returned object.

## Parameters

- `view`: The view whose preceding view in the key view loop to seek.

## See Also

### Managing the Key View Loop
- [func selectKeyView(following: NSView)](./selectkeyview%28following%29.md)
  Gives key view status to the view that follows the given view.
- [func selectPreviousKeyView(Any?)](./selectpreviouskeyview%28_%29.md)
  Searches for a candidate previous key view and, if it finds one, tries to make it the first responder.
- [func selectNextKeyView(Any?)](./selectnextkeyview%28_%29.md)
  Searches for a candidate next key view and, if it finds one, tries to make it the first responder.
- [var keyViewSelectionDirection: NSWindow.SelectionDirection](./keyviewselectiondirection.md)
  The direction the window is currently using to change the key view.
- [var autorecalculatesKeyViewLoop: Bool](./autorecalculateskeyviewloop.md)
  A Boolean value that indicates whether the window automatically recalculates the key view loop when views are added.
- [func recalculateKeyViewLoop()](./recalculatekeyviewloop%28%29.md)
  Marks the key view loop as “dirty” and in need of recalculation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/selectkeyview(preceding:))*