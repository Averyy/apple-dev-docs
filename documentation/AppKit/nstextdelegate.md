# NSTextDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of optional methods implemented by the delegate of an [`NSText`](nstext.md) object to edit text and change text formats.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSTextDelegate : NSObjectProtocol
```

## Topics

### Changing text formatting
- [func textDidChange(Notification)](nstextdelegate/textdidchange(_:).md)
  Informs the delegate that the text object has changed its characters or formatting attributes.
### Editing text
- [func textShouldBeginEditing(NSText) -> Bool](nstextdelegate/textshouldbeginediting(_:).md)
  Invoked when a text object begins to change its text, this method requests permission for `aTextObject` to begin editing.
- [func textDidBeginEditing(Notification)](nstextdelegate/textdidbeginediting(_:).md)
  Informs the delegate that the text object has begun editing (that the user has begun changing it).
- [func textShouldEndEditing(NSText) -> Bool](nstextdelegate/textshouldendediting(_:).md)
  Invoked from a text object’s implementation of [`resignFirstResponder()`](nsresponder/resignfirstresponder().md), this method requests permission for `aTextObject` to end editing.
- [func textDidEndEditing(Notification)](nstextdelegate/textdidendediting(_:).md)
  Informs the delegate that the text object has finished editing (that it has resigned first responder status).

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [NSTextViewDelegate](nstextviewdelegate.md)
### Conforming Types
- [NSOutlineView](nsoutlineview.md)
- [NSTableView](nstableview.md)

## See Also

- [class NSTextField](nstextfield.md)
  Text the user can select or edit to send an action message to a target when the user presses the Return key.
- [protocol NSTextFieldDelegate](nstextfielddelegate.md)
  A protocol that a text field delegate can use to control its field editor action menu.
- [class NSTextView](nstextview.md)
  A view that draws text and handles user interactions with that text.
- [protocol NSTextViewDelegate](nstextviewdelegate.md)
  A set of optional methods that text view delegates can use to manage selection, set text attributes, work with the spell checker, and more.
- [class NSText](nstext.md)
  The most general programmatic interface for objects that manage text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextdelegate)*