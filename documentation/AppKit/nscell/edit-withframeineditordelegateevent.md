# edit(withFrame:in:editor:delegate:event:)

**Framework**: AppKit  
**Kind**: method

Begins editing of the receiver’s text using the specified field editor.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func edit(withFrame rect: NSRect, in controlView: NSView, editor textObj: NSText, delegate: Any?, event: NSEvent?)
```

#### Discussion

If the receiver isn’t a text-type `NSCell` object, no editing is performed. Otherwise, the field editor (`textObj`) is sized to `aRect` and its superview is set to `controlView`, so it exactly covers the receiver. The field editor is then activated and editing begins. It’s the responsibility of the delegate to end editing when responding to [`textShouldEndEditing(_:)`](nstextdelegate/textshouldendediting(_:).md). Upon ending the editing session, the delegate should remove any data from the field editor.

## Parameters

- `rect`: The bounding rectangle of the cell.
- `controlView`: The control that manages the cell.
- `textObj`: The field editor to use for editing the cell.
- `delegate`: The object to use as a delegate for the field editor (  parameter). This delegate object receives various   delegation and notification methods during the course of editing the cell’s contents.
- `event`: The   event that initiated the editing behavior.

## See Also

- [func select(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, start: Int, length: Int)](nscell/select(withframe:in:editor:delegate:start:length:).md)
  Selects the specified text range in the cell’s field editor.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/edit(withframe:in:editor:delegate:event:))*