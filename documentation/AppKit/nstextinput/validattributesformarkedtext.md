# validAttributesForMarkedText

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of names for the attributes supported by the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```objc
- (NSArray *) validAttributesForMarkedText;
```

## Return Value

An array of `NSString` objects representing names for the supported attributes.

## Discussion

The input server may choose to use some of these attributes in the text it inserts or in marked text. Returns an empty array if no attributes are supported. See NSAttributedString Additions for the set of string constants that you could return in the array.

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
- [- attributedSubstringFromRange:](./attributedsubstringfromrange_.md)
  Returns an attributed string derived from the given range in the receiver’s text storage.
- [- insertText:](./inserttext_.md)
  Inserts the given string into the receiver’s text storage.
- [- characterIndexForPoint:](./characterindexforpoint_.md)
  Returns the index of the character whose frame rectangle includes the given point.
- [- firstRectForCharacterRange:](./firstrectforcharacterrange_.md)
  Returns the first frame rectangle for characters in the given range, in screen coordinates.
- [- doCommandBySelector:](./docommandbyselector_.md)
  Invokes the given selector if possible.
- [- conversationIdentifier](./conversationidentifier.md)
  Returns a number used to identify the receiver’s context to the input server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinput/validattributesformarkedtext)*