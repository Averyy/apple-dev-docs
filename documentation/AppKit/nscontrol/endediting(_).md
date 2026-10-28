# endEditing(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Ends the editing of text in the receiver using the specified field editor.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func endEditing(_ textObj: NSText)
```

```objc
- (void) endEditing:(NSText *) textObj;
```

## Discussion

Ends any editing of text that began with a call to [`edit(withFrame:editor:delegate:event:)`](./edit%28withframe,editor,delegate,event%29.md) or [`select(withFrame:editor:delegate:start:length:)`](./select%28withframe,editor,delegate,start,length%29.md).

## Parameters

- `textObj`: The field editor currently handling the editing of the cell’s content.

## See Also

### Managing the Field Editor
- [func abortEditing() -> Bool](./abortediting%28%29.md)
  Terminates the current editing operation and discards any edited text.
- [func currentEditor() -> NSText?](./currenteditor%28%29.md)
  Returns the current field editor for the control.
- [func validateEditing()](./validateediting%28%29.md)
  Validates changes to any user-typed text.
- [func edit(withFrame: NSRect, editor: NSText, delegate: Any?, event: NSEvent)](./edit%28withframe,editor,delegate,event%29.md)
  Begins editing of the receiver’s text using the specified field editor.
- [func select(withFrame: NSRect, editor: NSText, delegate: Any?, start: Int, length: Int)](./select%28withframe,editor,delegate,start,length%29.md)
  Selects the specified text range in the receiver’s field editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/endediting(_:))*