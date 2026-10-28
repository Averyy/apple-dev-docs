# layoutManagerOwnsFirstResponder(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Indicates whether the first responder in the specified window is a text view for the layout manager.

**Availability**:
- macOS

## Declaration

```swift
func layoutManagerOwnsFirstResponder(in window: NSWindow) -> Bool
```

```objc
- (BOOL) layoutManagerOwnsFirstResponderInWindow:(NSWindow *) window;
```

## Return Value

[`true`](../../Swift/true.md) if the first responder in `window` is a text view associated with the receiver; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `window`: The window whose first responder is tested.

## See Also

### Managing the responder chain
- [var firstTextView: NSTextView?](./firsttextview.md)
  The first text view in the layout manager’s series of text views.
- [var textViewForBeginningOfSelection: NSTextView?](./textviewforbeginningofselection.md)
  The text view that contains the first glyph in the selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/layoutmanagerownsfirstresponder(in:))*