# sendsActionOnEndEditing

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell’s control object sends its action message when the user finishes editing the cell’s text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var sendsActionOnEndEditing: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the control sends its action message when editing is complete. Editing is complete when the user does one of the following:

- Presses the Return key
- Presses the Tab key to move out of the field
- Clicks another text field

When the value is [`false`](https://developer.apple.com/documentation/Swift/false), the control sends its action message only when the user presses the Return key.

## See Also

- [func edit(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, event: NSEvent?)](nscell/edit(withframe:in:editor:delegate:event:).md)
  Begins editing of the receiver’s text using the specified field editor.
- [func select(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, start: Int, length: Int)](nscell/select(withframe:in:editor:delegate:start:length:).md)
  Selects the specified text range in the cell’s field editor.
- [func endEditing(NSText)](nscell/endediting(_:).md)
  Ends the editing of text in the receiver using the specified field editor.
- [var wantsNotificationForMarkedText: Bool](nscell/wantsnotificationformarkedtext.md)
  A Boolean value indicating whether the cell’s field editor should post text change notifications.
- [func fieldEditor(for: NSView) -> NSTextView?](nscell/fieldeditor(for:).md)
  Returns a custom field editor for editing in the view.
- [var usesSingleLineMode: Bool](nscell/usessinglelinemode.md)
  A Boolean value indicating whether the cell restricts layout and rendering of text to a single line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/sendsactiononendediting)*