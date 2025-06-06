# layoutManagerOwnsFirstResponder(in:)

**Framework**: AppKit  
**Kind**: method

Indicates whether the first responder in the specified window is a text view for the layout manager.

**Availability**:
- macOS ?+

## Declaration

```swift
func layoutManagerOwnsFirstResponder(in window: NSWindow) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the first responder in `window` is a text view associated with the receiver; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `window`: The window whose first responder is tested.

## See Also

- [var firstTextView: NSTextView?](nslayoutmanager/firsttextview.md)
  The first text view in the layout manager’s series of text views.
- [var textViewForBeginningOfSelection: NSTextView?](nslayoutmanager/textviewforbeginningofselection.md)
  The text view that contains the first glyph in the selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/layoutmanagerownsfirstresponder(in:))*