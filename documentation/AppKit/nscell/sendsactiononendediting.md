# sendsActionOnEndEditing

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell’s control object sends its action message when the user finishes editing the cell’s text.

**Availability**:
- macOS

## Declaration

```swift
var sendsActionOnEndEditing: Bool { get set }
```

```objc
@property BOOL sendsActionOnEndEditing;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the control sends its action message when editing is complete. Editing is complete when the user does one of the following:

- Presses the Return key
- Presses the Tab key to move out of the field
- Clicks another text field

When the value is [`false`](../../Swift/false.md), the control sends its action message only when the user presses the Return key.

## See Also

### Editing and Selecting Text
- [func edit(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, event: NSEvent?)](./edit%28withframe,in,editor,delegate,event%29.md)
  Begins editing of the receiver’s text using the specified field editor.
- [func select(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, start: Int, length: Int)](./select%28withframe,in,editor,delegate,start,length%29.md)
  Selects the specified text range in the cell’s field editor.
- [func endEditing(NSText)](./endediting%28_%29.md)
  Ends the editing of text in the receiver using the specified field editor.
- [var wantsNotificationForMarkedText: Bool](./wantsnotificationformarkedtext.md)
  A Boolean value indicating whether the cell’s field editor should post text change notifications.
- [func fieldEditor(for: NSView) -> NSTextView?](./fieldeditor%28for%29.md)
  Returns a custom field editor for editing in the view.
- [var usesSingleLineMode: Bool](./usessinglelinemode.md)
  A Boolean value indicating whether the cell restricts layout and rendering of text to a single line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/sendsactiononendediting)*