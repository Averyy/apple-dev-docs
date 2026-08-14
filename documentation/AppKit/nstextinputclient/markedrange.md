# markedRange()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the range of the marked text.

**Availability**:
- macOS ?+

## Declaration

```swift
func markedRange() -> NSRange
```

#### Return Value

The range of marked text or `{NSNotFound, 0}` if there is no marked range.

#### Discussion

The returned range measures from the start of the receiver’s text storage. The return value’s `location` is `NSNotFound` and its `length` is 0 if and only if [`hasMarkedText()`](nstextinputclient/hasmarkedtext().md) returns [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func hasMarkedText() -> Bool](nstextinputclient/hasmarkedtext.md)
  Returns a Boolean value indicating whether the receiver has marked text.
- [func selectedRange() -> NSRange](nstextinputclient/selectedrange.md)
  Returns the range of selected text.
- [func setMarkedText(Any, selectedRange: NSRange, replacementRange: NSRange)](nstextinputclient/setmarkedtext(_:selectedrange:replacementrange:).md)
  Replaces a specified range in the receiver’s text storage with the given string and sets the selection.
- [func unmarkText()](nstextinputclient/unmarktext.md)
  Unmarks the marked text.
- [func validAttributesForMarkedText() -> [NSAttributedString.Key]](nstextinputclient/validattributesformarkedtext.md)
  Returns an array of attribute names recognized by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/markedrange())*