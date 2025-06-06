# endEditing(_:)

**Framework**: AppKit  
**Kind**: method

Ends the editing of text in the receiver using the specified field editor.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func endEditing(_ textObj: NSText)
```

#### Discussion

Ends any editing of text that began with a call to [`edit(withFrame:editor:delegate:event:)`](nscontrol/edit(withframe:editor:delegate:event:).md) or [`select(withFrame:editor:delegate:start:length:)`](nscontrol/select(withframe:editor:delegate:start:length:).md).

## Parameters

- `textObj`: The field editor currently handling the editing of the cell’s content.

## See Also

- [func abortEditing() -> Bool](nscontrol/abortediting.md)
  Terminates the current editing operation and discards any edited text.
- [func currentEditor() -> NSText?](nscontrol/currenteditor.md)
  Returns the current field editor for the control.
- [func validateEditing()](nscontrol/validateediting.md)
  Validates changes to any user-typed text.
- [func edit(withFrame: NSRect, editor: NSText, delegate: Any?, event: NSEvent)](nscontrol/edit(withframe:editor:delegate:event:).md)
  Begins editing of the receiver’s text using the specified field editor.
- [func select(withFrame: NSRect, editor: NSText, delegate: Any?, start: Int, length: Int)](nscontrol/select(withframe:editor:delegate:start:length:).md)
  Selects the specified text range in the receiver’s field editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/endediting(_:))*