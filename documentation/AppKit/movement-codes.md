# Movement Codes

**Framework**: AppKit

The reason for a change of editing focus among text fields.

## Overview

These constants are the possible values for the `NSTextMovement` key of the [`didEndEditingNotification`](./nstext/didendeditingnotification.md) `userInfo` dictionary. The field editor makes sure that these are the values sent when the user presses the Tab, Backtab, or Return key while editing, in essence describing why the user is leaving the field. The control then uses this information to decide where to send focus next.

## Topics

### Deprecated
- [Deprecated symbols](./movement-codes-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## See Also

### Constants
- [enum NSTextAlignment](./nstextalignment.md)
  Constants that specify text alignment.
- [enum NSWritingDirection](./nswritingdirection.md)
  Constants that specify the writing direction.
- [Common Unicode Characters](./common-unicode-characters.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/movement-codes)*