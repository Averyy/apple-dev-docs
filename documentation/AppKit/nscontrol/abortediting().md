# abortEditing()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Terminates the current editing operation and discards any edited text.

**Availability**:
- macOS

## Declaration

```swift
func abortEditing() -> Bool
```

```objc
- (BOOL) abortEditing;
```

## Return Value

[`true`](../../Swift/true.md) if there was a field editor associated with the control; otherwise, [`false`](../../Swift/false.md).

## Discussion

If there was a field editor, this method removes the field editor’s delegate.

Because the control discards any edits, it doesn’t call [`controlTextDidEndEditing(_:)`](../nscontroltexteditingdelegate/controltextdidendediting%28_%29.md).

## See Also

### Managing the Field Editor
- [func currentEditor() -> NSText?](./currenteditor%28%29.md)
  Returns the current field editor for the control.
- [func validateEditing()](./validateediting%28%29.md)
  Validates changes to any user-typed text.
- [func edit(withFrame: NSRect, editor: NSText, delegate: Any?, event: NSEvent)](./edit%28withframe,editor,delegate,event%29.md)
  Begins editing of the receiver’s text using the specified field editor.
- [func endEditing(NSText)](./endediting%28_%29.md)
  Ends the editing of text in the receiver using the specified field editor.
- [func select(withFrame: NSRect, editor: NSText, delegate: Any?, start: Int, length: Int)](./select%28withframe,editor,delegate,start,length%29.md)
  Selects the specified text range in the receiver’s field editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/abortediting())*