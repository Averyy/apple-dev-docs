# validateEditing()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Validates changes to any user-typed text.

**Availability**:
- macOS

## Declaration

```swift
func validateEditing()
```

```objc
- (void) validateEditing;
```

## Discussion

Validation sets the object value of the cell to the current contents of the cell’s editor (the [`NSText`](../nstext.md) object used for editing), storing it as a simple [`NSString`](../../Foundation/nsstring.md) or an attributed string object based on the attributes of the editor.

## See Also

### Managing the Field Editor
- [func abortEditing() -> Bool](./abortediting%28%29.md)
  Terminates the current editing operation and discards any edited text.
- [func currentEditor() -> NSText?](./currenteditor%28%29.md)
  Returns the current field editor for the control.
- [func edit(withFrame: NSRect, editor: NSText, delegate: Any?, event: NSEvent)](./edit%28withframe,editor,delegate,event%29.md)
  Begins editing of the receiver’s text using the specified field editor.
- [func endEditing(NSText)](./endediting%28_%29.md)
  Ends the editing of text in the receiver using the specified field editor.
- [func select(withFrame: NSRect, editor: NSText, delegate: Any?, start: Int, length: Int)](./select%28withframe,editor,delegate,start,length%29.md)
  Selects the specified text range in the receiver’s field editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/validateediting())*