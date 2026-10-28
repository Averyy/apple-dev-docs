# wantsNotificationForMarkedText

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell’s field editor should post text change notifications.

**Availability**:
- macOS

## Declaration

```swift
var wantsNotificationForMarkedText: Bool { get }
```

```objc
@property (readonly) BOOL wantsNotificationForMarkedText;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the field editor should post text notification changes while editing marked text. When the value is NO, the field editor should delay notifications until the marked text is confirmed.

The default value of this property is [`false`](../../Swift/false.md). Subclasses can override the property and change the value as appropriate.

## See Also

### Editing and Selecting Text
- [func edit(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, event: NSEvent?)](./edit%28withframe,in,editor,delegate,event%29.md)
  Begins editing of the receiver’s text using the specified field editor.
- [func select(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, start: Int, length: Int)](./select%28withframe,in,editor,delegate,start,length%29.md)
  Selects the specified text range in the cell’s field editor.
- [var sendsActionOnEndEditing: Bool](./sendsactiononendediting.md)
  A Boolean value indicating whether the cell’s control object sends its action message when the user finishes editing the cell’s text.
- [func endEditing(NSText)](./endediting%28_%29.md)
  Ends the editing of text in the receiver using the specified field editor.
- [func fieldEditor(for: NSView) -> NSTextView?](./fieldeditor%28for%29.md)
  Returns a custom field editor for editing in the view.
- [var usesSingleLineMode: Bool](./usessinglelinemode.md)
  A Boolean value indicating whether the cell restricts layout and rendering of text to a single line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/wantsnotificationformarkedtext)*