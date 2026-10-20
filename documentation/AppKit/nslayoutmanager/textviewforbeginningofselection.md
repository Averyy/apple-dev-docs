# textViewForBeginningOfSelection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text view that contains the first glyph in the selection.

**Availability**:
- macOS

## Declaration

```swift
unowned(unsafe) var textViewForBeginningOfSelection: NSTextView? { get }
```

```objc
@property (assign, readonly, nullable) NSTextView * textViewForBeginningOfSelection;
```

#### Discussion

This property does not cause layout if the beginning of the selected range is not yet laid out.

## See Also

### Managing the responder chain
- [func layoutManagerOwnsFirstResponder(in: NSWindow) -> Bool](./layoutmanagerownsfirstresponder%28in%29.md)
  Indicates whether the first responder in the specified window is a text view for the layout manager.
- [var firstTextView: NSTextView?](./firsttextview.md)
  The first text view in the layout manager’s series of text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/textviewforbeginningofselection)*