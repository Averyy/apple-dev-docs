# validateEditing()

**Framework**: AppKit  
**Kind**: method

Validates changes to any user-typed text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func validateEditing()
```

#### Discussion

Validation sets the object value of the cell to the current contents of the cell’s editor (the [`NSText`](nstext.md) object used for editing), storing it as a simple [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) or an attributed string object based on the attributes of the editor.

## See Also

- [func abortEditing() -> Bool](nscontrol/abortediting.md)
  Terminates the current editing operation and discards any edited text.
- [func currentEditor() -> NSText?](nscontrol/currenteditor.md)
  Returns the current field editor for the control.
- [func edit(withFrame: NSRect, editor: NSText, delegate: Any?, event: NSEvent)](nscontrol/edit(withframe:editor:delegate:event:).md)
  Begins editing of the receiver’s text using the specified field editor.
- [func endEditing(NSText)](nscontrol/endediting(_:).md)
  Ends the editing of text in the receiver using the specified field editor.
- [func select(withFrame: NSRect, editor: NSText, delegate: Any?, start: Int, length: Int)](nscontrol/select(withframe:editor:delegate:start:length:).md)
  Selects the specified text range in the receiver’s field editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/validateediting())*