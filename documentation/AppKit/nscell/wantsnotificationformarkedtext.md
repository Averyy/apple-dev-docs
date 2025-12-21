# wantsNotificationForMarkedText

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell’s field editor should post text change notifications.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var wantsNotificationForMarkedText: Bool { get }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the field editor should post text notification changes while editing marked text. When the value is NO, the field editor should delay notifications until the marked text is confirmed.

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false). Subclasses can override the property and change the value as appropriate.

## See Also

- [func edit(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, event: NSEvent?)](nscell/edit(withframe:in:editor:delegate:event:).md)
  Begins editing of the receiver’s text using the specified field editor.
- [func select(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, start: Int, length: Int)](nscell/select(withframe:in:editor:delegate:start:length:).md)
  Selects the specified text range in the cell’s field editor.
- [var sendsActionOnEndEditing: Bool](nscell/sendsactiononendediting.md)
  A Boolean value indicating whether the cell’s control object sends its action message when the user finishes editing the cell’s text.
- [func endEditing(NSText)](nscell/endediting(_:).md)
  Ends the editing of text in the receiver using the specified field editor.
- [func fieldEditor(for: NSView) -> NSTextView?](nscell/fieldeditor(for:).md)
  Returns a custom field editor for editing in the view.
- [var usesSingleLineMode: Bool](nscell/usessinglelinemode.md)
  A Boolean value indicating whether the cell restricts layout and rendering of text to a single line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/wantsnotificationformarkedtext)*