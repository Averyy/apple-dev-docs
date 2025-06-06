# Movement Codes

**Framework**: AppKit

The reason for a change of editing focus among text fields.

#### Overview

These constants are the possible values for the `NSTextMovement` key of the [`didEndEditingNotification`](nstext/didendeditingnotification.md) `userInfo` dictionary. The field editor makes sure that these are the values sent when the user presses the Tab, Backtab, or Return key while editing, in essence describing why the user is leaving the field. The control then uses this information to decide where to send focus next.

## Topics

### Constants
- [var NSIllegalTextMovement: Int](nsillegaltextmovement.md)
  Currently unused.
- [var NSReturnTextMovement: Int](nsreturntextmovement.md)
  The Return key was pressed.
- [var NSTabTextMovement: Int](nstabtextmovement.md)
  The Tab key was pressed.
- [var NSBacktabTextMovement: Int](nsbacktabtextmovement.md)
  The Backtab (Shift-Tab) key was pressed.
- [var NSLeftTextMovement: Int](nslefttextmovement.md)
  The left arrow key was pressed.
- [var NSRightTextMovement: Int](nsrighttextmovement.md)
  The right arrow key was pressed.
- [var NSUpTextMovement: Int](nsuptextmovement.md)
  The up arrow key was pressed.
- [var NSDownTextMovement: Int](nsdowntextmovement.md)
  The down arrow key was pressed.
- [var NSCancelTextMovement: Int](nscanceltextmovement.md)
  The user cancelled the completion.
- [var NSOtherTextMovement: Int](nsothertextmovement.md)
  The user performed some undefined action.

## See Also

- [enum NSTextAlignment](nstextalignment.md)
  Constants that specify text alignment.
- [enum NSWritingDirection](nswritingdirection.md)
  Constants that specify the writing direction.
- [Common Unicode Characters](common-unicode-characters.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/movement-codes)*