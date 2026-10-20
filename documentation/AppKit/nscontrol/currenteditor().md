# currentEditor()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the current field editor for the control.

**Availability**:
- macOS

## Declaration

```swift
func currentEditor() -> NSText?
```

```objc
- (NSText *) currentEditor;
```

#### Return Value

The field editor for the current control, or `nil` if the receiver does not have a field editor.

#### Discussion

When the receiver is a control displaying editable text (for example, a text field) and it is the first responder, it has a field editor, which is returned by this method. The field editor is a single [`NSTextView`](../nstextview.md) object that is shared among all the controls in a window for light text-editing needs. It is automatically instantiated when needed.

## See Also

### Managing the Field Editor
- [func abortEditing() -> Bool](./abortediting%28%29.md)
  Terminates the current editing operation and discards any edited text.
- [func validateEditing()](./validateediting%28%29.md)
  Validates changes to any user-typed text.
- [func edit(withFrame: NSRect, editor: NSText, delegate: Any?, event: NSEvent)](./edit%28withframe,editor,delegate,event%29.md)
  Begins editing of the receiver’s text using the specified field editor.
- [func endEditing(NSText)](./endediting%28_%29.md)
  Ends the editing of text in the receiver using the specified field editor.
- [func select(withFrame: NSRect, editor: NSText, delegate: Any?, start: Int, length: Int)](./select%28withframe,editor,delegate,start,length%29.md)
  Selects the specified text range in the receiver’s field editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/currenteditor())*