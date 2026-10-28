# doCommandBySelector:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invokes the given selector if possible.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```objc
- (void) doCommandBySelector:(SEL) selector;
```

## Discussion

If `selector` cannot be invoked, then [`doCommandBySelector:`](./docommandbyselector_.md) should not pass this message up the responder chain. `NSResponder` also implements this method, and it does forward uninvokable commands up the responder chain, but a text view should not. A text view implementing the [`NSTextInput`](../nstextinput.md) protocol inherits from `NSView`, which inherits from `NSResponder`, so your implementation of this method will override the one in `NSResponder`. It should not call `super`.

## Parameters

- `selector`: The selector to be invoked.

## See Also

### Related Documentation
- [func interpretKeyEvents([NSEvent])](../nsresponder/interpretkeyevents%28_%29.md)
  Handles a series of key events.
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
- [- firstRectForCharacterRange:](./firstrectforcharacterrange_.md)
  Returns the first frame rectangle for characters in the given range, in screen coordinates.
- [- conversationIdentifier](./conversationidentifier.md)
  Returns a number used to identify the receiver’s context to the input server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinput/docommandbyselector:)*