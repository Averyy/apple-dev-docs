# selectedRange()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the range of selected text.

**Availability**:
- macOS

## Declaration

```swift
func selectedRange() -> NSRange
```

```objc
- (NSRange) selectedRange;
```

#### Return Value

The range of selected text or `{NSNotFound, 0}` if there is no selection.

#### Discussion

The returned range measures from the start of the receiver’s text storage, that is, from 0 to the document length.

## See Also

### Handling marked text
- [func hasMarkedText() -> Bool](./hasmarkedtext%28%29.md)
  Returns a Boolean value indicating whether the receiver has marked text.
- [func markedRange() -> NSRange](./markedrange%28%29.md)
  Returns the range of the marked text.
- [func setMarkedText(Any, selectedRange: NSRange, replacementRange: NSRange)](./setmarkedtext%28_,selectedrange,replacementrange%29.md)
  Replaces a specified range in the receiver’s text storage with the given string and sets the selection.
- [func unmarkText()](./unmarktext%28%29.md)
  Unmarks the marked text.
- [func validAttributesForMarkedText() -> [NSAttributedString.Key]](./validattributesformarkedtext%28%29.md)
  Returns an array of attribute names recognized by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/selectedrange())*