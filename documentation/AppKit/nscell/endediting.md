# endEditing(_:)

**Framework**: AppKit  
**Kind**: method

Ends the editing of text in the receiver using the specified field editor.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func endEditing(_ textObj: NSText)
```

#### Discussion

Ends any editing of text that began with a call to [`edit(withFrame:in:editor:delegate:event:)`](nscell/edit(withframe:in:editor:delegate:event:).md) or  [`select(withFrame:in:editor:delegate:start:length:)`](nscell/select(withframe:in:editor:delegate:start:length:).md).

## Parameters

- `textObj`: The field editor currently handling the editing of the cell’s content.

## See Also

- [func edit(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, event: NSEvent?)](nscell/edit(withframe:in:editor:delegate:event:).md)
  Begins editing of the receiver’s text using the specified field editor.
- [func select(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, start: Int, length: Int)](nscell/select(withframe:in:editor:delegate:start:length:).md)
  Selects the specified text range in the cell’s field editor.
- [var sendsActionOnEndEditing: Bool](nscell/sendsactiononendediting.md)
  A Boolean value indicating whether the cell’s control object sends its action message when the user finishes editing the cell’s text.
- [var wantsNotificationForMarkedText: Bool](nscell/wantsnotificationformarkedtext.md)
  A Boolean value indicating whether the cell’s field editor should post text change notifications.
- [func fieldEditor(for: NSView) -> NSTextView?](nscell/fieldeditor(for:).md)
  Returns a custom field editor for editing in the view.
- [var usesSingleLineMode: Bool](nscell/usessinglelinemode.md)
  A Boolean value indicating whether the cell restricts layout and rendering of text to a single line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/endediting(_:))*