# edit(withFrame:editor:delegate:event:)

**Framework**: AppKit  
**Kind**: method

Begins editing of the receiver’s text using the specified field editor.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func edit(withFrame rect: NSRect, editor textObj: NSText, delegate: Any?, event: NSEvent)
```

#### Discussion

For a receiver that is a control with editable text (such as an [`NSTextField`](nstextfield.md) object), the field editor is sized to `aRect` and is then activated and editing begins. It’s the responsibility of the delegate to end editing when responding to [`control(_:textShouldEndEditing:)`](nscontroltexteditingdelegate/control(_:textshouldendediting:).md). Upon ending the editing session, the delegate should remove any data from the field editor.

## Parameters

- `rect`: The bounding rectangle of the control’s cell.
- `textObj`: The field editor to use.
- `delegate`: The object to use as a delegate for the field editor. This delegate object receives various   delegation and notification methods during the course of editing the cell’s contents.
- `event`: The   event that initiated the editing behavior.

## See Also

- [func abortEditing() -> Bool](nscontrol/abortediting.md)
  Terminates the current editing operation and discards any edited text.
- [func currentEditor() -> NSText?](nscontrol/currenteditor.md)
  Returns the current field editor for the control.
- [func validateEditing()](nscontrol/validateediting.md)
  Validates changes to any user-typed text.
- [func endEditing(NSText)](nscontrol/endediting(_:).md)
  Ends the editing of text in the receiver using the specified field editor.
- [func select(withFrame: NSRect, editor: NSText, delegate: Any?, start: Int, length: Int)](nscontrol/select(withframe:editor:delegate:start:length:).md)
  Selects the specified text range in the receiver’s field editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/edit(withframe:editor:delegate:event:))*