# firstTextView

**Framework**: AppKit  
**Kind**: property

The first text view in the layout manager’s series of text views.

**Availability**:
- macOS ?+

## Declaration

```swift
unowned(unsafe) var firstTextView: NSTextView? { get }
```

#### Discussion

This `NSTextView` object is the recipient of various `NSText` and `NSTextView` notifications.

## See Also

- [func layoutManagerOwnsFirstResponder(in: NSWindow) -> Bool](nslayoutmanager/layoutmanagerownsfirstresponder(in:).md)
  Indicates whether the first responder in the specified window is a text view for the layout manager.
- [var textViewForBeginningOfSelection: NSTextView?](nslayoutmanager/textviewforbeginningofselection.md)
  The text view that contains the first glyph in the selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/firsttextview)*