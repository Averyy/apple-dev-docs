# firstTextView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The first text view in the layout manager’s series of text views.

**Availability**:
- macOS

## Declaration

```swift
unowned(unsafe) var firstTextView: NSTextView? { get }
```

```objc
@property (assign, readonly, nullable) NSTextView * firstTextView;
```

#### Discussion

This `NSTextView` object is the recipient of various `NSText` and `NSTextView` notifications.

## See Also

### Managing the responder chain
- [func layoutManagerOwnsFirstResponder(in: NSWindow) -> Bool](./layoutmanagerownsfirstresponder%28in%29.md)
  Indicates whether the first responder in the specified window is a text view for the layout manager.
- [var textViewForBeginningOfSelection: NSTextView?](./textviewforbeginningofselection.md)
  The text view that contains the first glyph in the selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/firsttextview)*