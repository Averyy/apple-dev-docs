# edit(withFrame:in:editor:delegate:event:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Begins editing of the receiver’s text using the specified field editor.

**Availability**:
- macOS

## Declaration

```swift
func edit(withFrame rect: NSRect, in controlView: NSView, editor textObj: NSText, delegate: Any?, event: NSEvent?)
```

```objc
- (void) editWithFrame:(NSRect) rect inView:(NSView *) controlView editor:(NSText *) textObj delegate:(id) delegate event:(NSEvent *) event;
```

## Discussion

If the receiver isn’t a text-type `NSCell` object, no editing is performed. Otherwise, the field editor (`textObj`) is sized to `aRect` and its superview is set to `controlView`, so it exactly covers the receiver. The field editor is then activated and editing begins. It’s the responsibility of the delegate to end editing when responding to [`textShouldEndEditing(_:)`](../nstextdelegate/textshouldendediting%28_%29.md). Upon ending the editing session, the delegate should remove any data from the field editor.

## Parameters

- `rect`: The bounding rectangle of the cell.
- `controlView`: The control that manages the cell.
- `textObj`: The field editor to use for editing the cell.
- `delegate`: The object to use as a delegate for the field editor (`textObj` parameter). This delegate object receives various `NSText` delegation and notification methods during the course of editing the cell’s contents.
- `event`: The `NSLeftMouseDown` event that initiated the editing behavior.

## See Also

### Editing and Selecting Text
- [func select(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, start: Int, length: Int)](./select%28withframe,in,editor,delegate,start,length%29.md)
  Selects the specified text range in the cell’s field editor.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/edit(withframe:in:editor:delegate:event:))*