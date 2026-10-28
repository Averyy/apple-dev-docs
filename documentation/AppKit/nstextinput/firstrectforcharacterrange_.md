# firstRectForCharacterRange:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the first frame rectangle for characters in the given range, in screen coordinates.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```objc
- (NSRect) firstRectForCharacterRange:(NSRange) range;
```

## Return Value

The frame rectangle for the given range of characters.

## Discussion

If `theRange` spans multiple lines of text in the text view, the rectangle returned is the one for the characters in the first line. If the length of `theRange` is 0 (as it would be if there is nothing selected at the insertion point), the rectangle coincides with the insertion point, and its width is 0.

## Parameters

- `range`: The character range whose frame is returned.

## See Also

### Deprecated methods
- [- hasMarkedText](./hasmarkedtext.md)
  Returns a Boolean value indicating whether or not the receiver has marked text.
- [- markedRange](./markedrange.md)
  Returns the range of the marked text.
- [- selectedRange](./selectedrange.md)
  Returns the range of selected text.
- [- setMarkedText:selectedRange:](./setmarkedtext_selectedrange_.md)
  Replaces currently marked text in the receiver’s text storage with the given string and sets the selection to the given range, computed from the beginning of the marked text.
- [- unmarkText](./unmarktext.md)
  Removes any marking from pending input text and disposes of the marked text as it wishes. The text view should accept the marked text as if it had been inserted normally.
- [- validAttributesForMarkedText](./validattributesformarkedtext.md)
  Returns an array of names for the attributes supported by the receiver.
- [- attributedSubstringFromRange:](./attributedsubstringfromrange_.md)
  Returns an attributed string derived from the given range in the receiver’s text storage.
- [- insertText:](./inserttext_.md)
  Inserts the given string into the receiver’s text storage.
- [- characterIndexForPoint:](./characterindexforpoint_.md)
  Returns the index of the character whose frame rectangle includes the given point.
- [- doCommandBySelector:](./docommandbyselector_.md)
  Invokes the given selector if possible.
- [- conversationIdentifier](./conversationidentifier.md)
  Returns a number used to identify the receiver’s context to the input server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinput/firstrectforcharacterrange:)*