# select(withFrame:in:editor:delegate:start:length:)

**Framework**: AppKit  
**Kind**: method

Selects the specified text range in the cell’s field editor.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func select(withFrame rect: NSRect, in controlView: NSView, editor textObj: NSText, delegate: Any?, start selStart: Int, length selLength: Int)
```

#### Discussion

This method is similar to [`edit(withFrame:in:editor:delegate:event:)`](nscell/edit(withframe:in:editor:delegate:event:).md), except that it can be invoked in any situation, not only on a mouse-down event. This method returns without doing anything if `controlView`, `textObj`, or the receiver is `nil`, or if the receiver has no font set for it.

## Parameters

- `rect`: The bounding rectangle of the cell.
- `controlView`: The control that manages the cell.
- `textObj`: The field editor to use for editing the cell.
- `delegate`: The object to use as a delegate for the field editor (  parameter). This delegate object receives various   delegation and notification methods during the course of editing the cell’s contents.
- `selStart`: The start of the text selection.
- `selLength`: The length of the text range.

## See Also

- [func edit(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, event: NSEvent?)](nscell/edit(withframe:in:editor:delegate:event:).md)
  Begins editing of the receiver’s text using the specified field editor.
- [var sendsActionOnEndEditing: Bool](nscell/sendsactiononendediting.md)
  A Boolean value indicating whether the cell’s control object sends its action message when the user finishes editing the cell’s text.
- [func endEditing(NSText)](nscell/endediting(_:).md)
  Ends the editing of text in the receiver using the specified field editor.
- [var wantsNotificationForMarkedText: Bool](nscell/wantsnotificationformarkedtext.md)
  A Boolean value indicating whether the cell’s field editor should post text change notifications.
- [func fieldEditor(for: NSView) -> NSTextView?](nscell/fieldeditor(for:).md)
  Returns a custom field editor for editing in the view.
- [var usesSingleLineMode: Bool](nscell/usessinglelinemode.md)
  A Boolean value indicating whether the cell restricts layout and rendering of text to a single line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/select(withframe:in:editor:delegate:start:length:))*