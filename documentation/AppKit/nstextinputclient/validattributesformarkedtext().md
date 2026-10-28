# validAttributesForMarkedText()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns an array of attribute names recognized by the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func validAttributesForMarkedText() -> [NSAttributedString.Key]
```

```objc
- (NSArray<NSString *> *) validAttributesForMarkedText;
```

## Return Value

An array of `NSString` objects representing names for the supported attributes.

## Discussion

Returns an empty array if no attributes are supported. See NSAttributedString Application Kit Additions Reference for the set of string constants representing standard attributes.

## See Also

### Handling marked text
- [func hasMarkedText() -> Bool](./hasmarkedtext%28%29.md)
  Returns a Boolean value indicating whether the receiver has marked text.
- [func markedRange() -> NSRange](./markedrange%28%29.md)
  Returns the range of the marked text.
- [func selectedRange() -> NSRange](./selectedrange%28%29.md)
  Returns the range of selected text.
- [func setMarkedText(Any, selectedRange: NSRange, replacementRange: NSRange)](./setmarkedtext%28_,selectedrange,replacementrange%29.md)
  Replaces a specified range in the receiver’s text storage with the given string and sets the selection.
- [func unmarkText()](./unmarktext%28%29.md)
  Unmarks the marked text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/validattributesformarkedtext())*