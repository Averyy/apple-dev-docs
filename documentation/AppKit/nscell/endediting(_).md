# endEditing(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Ends the editing of text in the receiver using the specified field editor.

**Availability**:
- macOS

## Declaration

```swift
func endEditing(_ textObj: NSText)
```

```objc
- (void) endEditing:(NSText *) textObj;
```

#### Discussion

Ends any editing of text that began with a call to [`edit(withFrame:in:editor:delegate:event:)`](./edit%28withframe,in,editor,delegate,event%29.md) or  [`select(withFrame:in:editor:delegate:start:length:)`](./select%28withframe,in,editor,delegate,start,length%29.md).

## Parameters

- `textObj`: The field editor currently handling the editing of the cell’s content.

## See Also

### Editing and Selecting Text
- [func edit(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, event: NSEvent?)](./edit%28withframe,in,editor,delegate,event%29.md)
  Begins editing of the receiver’s text using the specified field editor.
- [func select(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, start: Int, length: Int)](./select%28withframe,in,editor,delegate,start,length%29.md)
  Selects the specified text range in the cell’s field editor.
- [var sendsActionOnEndEditing: Bool](./sendsactiononendediting.md)
  A Boolean value indicating whether the cell’s control object sends its action message when the user finishes editing the cell’s text.
- [var wantsNotificationForMarkedText: Bool](./wantsnotificationformarkedtext.md)
  A Boolean value indicating whether the cell’s field editor should post text change notifications.
- [func fieldEditor(for: NSView) -> NSTextView?](./fieldeditor%28for%29.md)
  Returns a custom field editor for editing in the view.
- [var usesSingleLineMode: Bool](./usessinglelinemode.md)
  A Boolean value indicating whether the cell restricts layout and rendering of text to a single line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/endediting(_:))*