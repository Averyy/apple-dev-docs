# fieldEditor(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a custom field editor for editing in the view.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func fieldEditor(for controlView: NSView) -> NSTextView?
```

```objc
- (NSTextView *) fieldEditorForView:(NSView *) controlView;
```

## Return Value

A custom field editor. The field editor must have [`isFieldEditor`](../nstextview/isfieldeditor.md) set to [`true`](../../Swift/true.md).

## Discussion

This is an override point for `NSCell` subclasses designed to use their own custom field editors. This message is sent to the selected cell of `aControlView` using the [`NSWindow`](../nswindow.md) method in [`fieldEditor(_:for:)`](../nswindow/fieldeditor%28_,for%29.md).

Returning non-`nil` from this method indicates skipping the standard field editor querying processes including [`windowWillReturnFieldEditor(_:to:)`](../nswindowdelegate/windowwillreturnfieldeditor%28_,to%29.md) delegation.

The default implementation returns `nil`.

## Parameters

- `controlView`: The view containing cells that require a custom field editor.

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
- [var wantsNotificationForMarkedText: Bool](./wantsnotificationformarkedtext.md)
  A Boolean value indicating whether the cell’s field editor should post text change notifications.
- [var usesSingleLineMode: Bool](./usessinglelinemode.md)
  A Boolean value indicating whether the cell restricts layout and rendering of text to a single line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/fieldeditor(for:))*