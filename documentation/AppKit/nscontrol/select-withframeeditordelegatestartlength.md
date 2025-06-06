# select(withFrame:editor:delegate:start:length:)

**Framework**: AppKit  
**Kind**: method

Selects the specified text range in the receiver’s field editor.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func select(withFrame rect: NSRect, editor textObj: NSText, delegate: Any?, start selStart: Int, length selLength: Int)
```

#### Discussion

This method is similar to [`edit(withFrame:editor:delegate:event:)`](nscontrol/edit(withframe:editor:delegate:event:).md), except that it can be invoked in any situation, not only on a mouse-down event. This method returns without doing anything if `textObj` or the receiver is `nil`, or if the receiver has no font set for it.

## Parameters

- `rect`: The bounding rectangle of the control’s cell.
- `textObj`: The field editor to use.
- `delegate`: The object to use as a delegate for the field editor. This delegate object receives various   delegation and notification methods during the course of editing the cell’s contents.
- `selStart`: The start of the text selection.
- `selLength`: The length of the text range.

## See Also

- [func abortEditing() -> Bool](nscontrol/abortediting.md)
  Terminates the current editing operation and discards any edited text.
- [func currentEditor() -> NSText?](nscontrol/currenteditor.md)
  Returns the current field editor for the control.
- [func validateEditing()](nscontrol/validateediting.md)
  Validates changes to any user-typed text.
- [func edit(withFrame: NSRect, editor: NSText, delegate: Any?, event: NSEvent)](nscontrol/edit(withframe:editor:delegate:event:).md)
  Begins editing of the receiver’s text using the specified field editor.
- [func endEditing(NSText)](nscontrol/endediting(_:).md)
  Ends the editing of text in the receiver using the specified field editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/select(withframe:editor:delegate:start:length:))*