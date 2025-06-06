# abortEditing()

**Framework**: AppKit  
**Kind**: method

Terminates the current editing operation and discards any edited text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func abortEditing() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if there was a field editor associated with the control; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If there was a field editor, this method removes the field editor’s delegate.

Because the control discards any edits, it doesn’t call [`controlTextDidEndEditing(_:)`](nscontroltexteditingdelegate/controltextdidendediting(_:).md).

## See Also

- [func currentEditor() -> NSText?](nscontrol/currenteditor.md)
  Returns the current field editor for the control.
- [func validateEditing()](nscontrol/validateediting.md)
  Validates changes to any user-typed text.
- [func edit(withFrame: NSRect, editor: NSText, delegate: Any?, event: NSEvent)](nscontrol/edit(withframe:editor:delegate:event:).md)
  Begins editing of the receiver’s text using the specified field editor.
- [func endEditing(NSText)](nscontrol/endediting(_:).md)
  Ends the editing of text in the receiver using the specified field editor.
- [func select(withFrame: NSRect, editor: NSText, delegate: Any?, start: Int, length: Int)](nscontrol/select(withframe:editor:delegate:start:length:).md)
  Selects the specified text range in the receiver’s field editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/abortediting())*