# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [- hasMarkedText](./nstextinput/hasmarkedtext.md)
  Returns a Boolean value indicating whether or not the receiver has marked text.
- [- markedRange](./nstextinput/markedrange.md)
  Returns the range of the marked text.
- [- selectedRange](./nstextinput/selectedrange.md)
  Returns the range of selected text.
- [- setMarkedText:selectedRange:](./nstextinput/setmarkedtext_selectedrange_.md)
  Replaces currently marked text in the receiver’s text storage with the given string and sets the selection to the given range, computed from the beginning of the marked text.
- [- unmarkText](./nstextinput/unmarktext.md)
  Removes any marking from pending input text and disposes of the marked text as it wishes. The text view should accept the marked text as if it had been inserted normally.
- [- validAttributesForMarkedText](./nstextinput/validattributesformarkedtext.md)
  Returns an array of names for the attributes supported by the receiver.
- [- attributedSubstringFromRange:](./nstextinput/attributedsubstringfromrange_.md)
  Returns an attributed string derived from the given range in the receiver’s text storage.
- [- insertText:](./nstextinput/inserttext_.md)
  Inserts the given string into the receiver’s text storage.
- [- characterIndexForPoint:](./nstextinput/characterindexforpoint_.md)
  Returns the index of the character whose frame rectangle includes the given point.
- [- firstRectForCharacterRange:](./nstextinput/firstrectforcharacterrange_.md)
  Returns the first frame rectangle for characters in the given range, in screen coordinates.
- [- doCommandBySelector:](./nstextinput/docommandbyselector_.md)
  Invokes the given selector if possible.
- [- conversationIdentifier](./nstextinput/conversationidentifier.md)
  Returns a number used to identify the receiver’s context to the input server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinput-deprecated-symbols)*