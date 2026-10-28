# select(withFrame:editor:delegate:start:length:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the specified text range in the receiver’s field editor.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func select(withFrame rect: NSRect, editor textObj: NSText, delegate: Any?, start selStart: Int, length selLength: Int)
```

```objc
- (void) selectWithFrame:(NSRect) rect editor:(NSText *) textObj delegate:(id) delegate start:(NSInteger) selStart length:(NSInteger) selLength;
```

## Discussion

This method is similar to [`edit(withFrame:editor:delegate:event:)`](./edit%28withframe,editor,delegate,event%29.md), except that it can be invoked in any situation, not only on a mouse-down event. This method returns without doing anything if `textObj` or the receiver is `nil`, or if the receiver has no font set for it.

## Parameters

- `rect`: The bounding rectangle of the control’s cell.
- `textObj`: The field editor to use.
- `delegate`: The object to use as a delegate for the field editor. This delegate object receives various [`NSText`](../nstext.md) delegation and notification methods during the course of editing the cell’s contents.
- `selStart`: The start of the text selection.
- `selLength`: The length of the text range.

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
- [func endEditing(NSText)](./endediting%28_%29.md)
  Ends the editing of text in the receiver using the specified field editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/select(withframe:editor:delegate:start:length:))*