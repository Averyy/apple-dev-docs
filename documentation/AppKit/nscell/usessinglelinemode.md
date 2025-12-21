# usesSingleLineMode

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell restricts layout and rendering of text to a single line.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var usesSingleLineMode: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), text layout and rendering is restricted to a single line. In addition, the cell ignores the return value from [`wraps`](nscell/wraps.md), interprets [`NSLineBreakMode.byWordWrapping`](nslinebreakmode/bywordwrapping.md) and [`NSLineBreakMode.byCharWrapping`](nslinebreakmode/bycharwrapping.md) returned by [`lineBreakMode`](nscell/linebreakmode.md) as [`NSLineBreakMode.byClipping`](nslinebreakmode/byclipping.md), and configures the field editor to ignore key binding commands that insert paragraph and line separators.

The field editor bound to a single-line cell filters out paragraph and line separator insertion from user actions. Cells in single-line mode use the fixed baseline layout. The text baseline position is determined solely by the control size regardless of content font style or size.

## See Also

- [func edit(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, event: NSEvent?)](nscell/edit(withframe:in:editor:delegate:event:).md)
  Begins editing of the receiver’s text using the specified field editor.
- [func select(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, start: Int, length: Int)](nscell/select(withframe:in:editor:delegate:start:length:).md)
  Selects the specified text range in the cell’s field editor.
- [var sendsActionOnEndEditing: Bool](nscell/sendsactiononendediting.md)
  A Boolean value indicating whether the cell’s control object sends its action message when the user finishes editing the cell’s text.
- [func endEditing(NSText)](nscell/endediting(_:).md)
  Ends the editing of text in the receiver using the specified field editor.
- [var wantsNotificationForMarkedText: Bool](nscell/wantsnotificationformarkedtext.md)
  A Boolean value indicating whether the cell’s field editor should post text change notifications.
- [func fieldEditor(for: NSView) -> NSTextView?](nscell/fieldeditor(for:).md)
  Returns a custom field editor for editing in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/usessinglelinemode)*