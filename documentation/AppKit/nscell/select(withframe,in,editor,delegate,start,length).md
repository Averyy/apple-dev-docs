# select(withFrame:in:editor:delegate:start:length:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the specified text range in the cell’s field editor.

**Availability**:
- macOS

## Declaration

```swift
func select(withFrame rect: NSRect, in controlView: NSView, editor textObj: NSText, delegate: Any?, start selStart: Int, length selLength: Int)
```

```objc
- (void) selectWithFrame:(NSRect) rect inView:(NSView *) controlView editor:(NSText *) textObj delegate:(id) delegate start:(NSInteger) selStart length:(NSInteger) selLength;
```

## Discussion

This method is similar to [`edit(withFrame:in:editor:delegate:event:)`](./edit%28withframe,in,editor,delegate,event%29.md), except that it can be invoked in any situation, not only on a mouse-down event. This method returns without doing anything if `controlView`, `textObj`, or the receiver is `nil`, or if the receiver has no font set for it.

## Parameters

- `rect`: The bounding rectangle of the cell.
- `controlView`: The control that manages the cell.
- `textObj`: The field editor to use for editing the cell.
- `delegate`: The object to use as a delegate for the field editor (`textObj` parameter). This delegate object receives various `NSText` delegation and notification methods during the course of editing the cell’s contents.
- `selStart`: The start of the text selection.
- `selLength`: The length of the text range.

## See Also

### Editing and Selecting Text
- [func edit(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, event: NSEvent?)](./edit%28withframe,in,editor,delegate,event%29.md)
  Begins editing of the receiver’s text using the specified field editor.
- [var sendsActionOnEndEditing: Bool](./sendsactiononendediting.md)
  A Boolean value indicating whether the cell’s control object sends its action message when the user finishes editing the cell’s text.
- [func endEditing(NSText)](./endediting%28_%29.md)
  Ends the editing of text in the receiver using the specified field editor.
- [var wantsNotificationForMarkedText: Bool](./wantsnotificationformarkedtext.md)
  A Boolean value indicating whether the cell’s field editor should post text change notifications.
- [func fieldEditor(for: NSView) -> NSTextView?](./fieldeditor%28for%29.md)
  Returns a custom field editor for editing in the view.
- [var usesSingleLineMode: Bool](./usessinglelinemode.md)
  A Boolean value indicating whether the cell restricts layout and rendering of text to a single line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/select(withframe:in:editor:delegate:start:length:))*