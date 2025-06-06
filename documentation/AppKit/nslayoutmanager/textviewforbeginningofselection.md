# textViewForBeginningOfSelection

**Framework**: AppKit  
**Kind**: property

The text view that contains the first glyph in the selection.

**Availability**:
- macOS ?+

## Declaration

```swift
unowned(unsafe) var textViewForBeginningOfSelection: NSTextView? { get }
```

#### Discussion

This property does not cause layout if the beginning of the selected range is not yet laid out.

## See Also

- [func layoutManagerOwnsFirstResponder(in: NSWindow) -> Bool](nslayoutmanager/layoutmanagerownsfirstresponder(in:).md)
  Indicates whether the first responder in the specified window is a text view for the layout manager.
- [var firstTextView: NSTextView?](nslayoutmanager/firsttextview.md)
  The first text view in the layout manager’s series of text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/textviewforbeginningofselection)*