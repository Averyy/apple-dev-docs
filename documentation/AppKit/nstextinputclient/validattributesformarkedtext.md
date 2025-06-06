# validAttributesForMarkedText()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns an array of attribute names recognized by the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func validAttributesForMarkedText() -> [NSAttributedString.Key]
```

#### Return Value

An array of `NSString` objects representing names for the supported attributes.

#### Discussion

Returns an empty array if no attributes are supported. See NSAttributedString Application Kit Additions Reference for the set of string constants representing standard attributes.

## See Also

- [func hasMarkedText() -> Bool](nstextinputclient/hasmarkedtext.md)
  Returns a Boolean value indicating whether the receiver has marked text.
- [func markedRange() -> NSRange](nstextinputclient/markedrange.md)
  Returns the range of the marked text.
- [func selectedRange() -> NSRange](nstextinputclient/selectedrange.md)
  Returns the range of selected text.
- [func setMarkedText(Any, selectedRange: NSRange, replacementRange: NSRange)](nstextinputclient/setmarkedtext(_:selectedrange:replacementrange:).md)
  Replaces a specified range in the receiver’s text storage with the given string and sets the selection.
- [func unmarkText()](nstextinputclient/unmarktext.md)
  Unmarks the marked text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/validattributesformarkedtext())*