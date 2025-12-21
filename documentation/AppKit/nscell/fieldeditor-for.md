# fieldEditor(for:)

**Framework**: AppKit  
**Kind**: method

Returns a custom field editor for editing in the view.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func fieldEditor(for controlView: NSView) -> NSTextView?
```

#### Return Value

A custom field editor. The field editor must have [`isFieldEditor`](nstextview/isfieldeditor.md) set to [`true`](https://developer.apple.com/documentation/Swift/true).

#### Discussion

This is an override point for `NSCell` subclasses designed to use their own custom field editors. This message is sent to the selected cell of `aControlView` using the [`NSWindow`](nswindow.md) method in [`fieldEditor(_:for:)`](nswindow/fieldeditor(_:for:).md).

Returning non-`nil` from this method indicates skipping the standard field editor querying processes including [`windowWillReturnFieldEditor(_:to:)`](nswindowdelegate/windowwillreturnfieldeditor(_:to:).md) delegation.

The default implementation returns `nil`.

## Parameters

- `controlView`: The view containing cells that require a custom field editor.

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
- [var usesSingleLineMode: Bool](nscell/usessinglelinemode.md)
  A Boolean value indicating whether the cell restricts layout and rendering of text to a single line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/fieldeditor(for:))*