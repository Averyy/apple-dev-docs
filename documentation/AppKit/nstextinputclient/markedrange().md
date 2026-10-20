# markedRange()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the range of the marked text.

**Availability**:
- macOS

## Declaration

```swift
func markedRange() -> NSRange
```

```objc
- (NSRange) markedRange;
```

#### Return Value

The range of marked text or `{NSNotFound, 0}` if there is no marked range.

#### Discussion

The returned range measures from the start of the receiver’s text storage. The return value’s `location` is `NSNotFound` and its `length` is 0 if and only if [`hasMarkedText()`](./hasmarkedtext%28%29.md) returns [`false`](../../Swift/false.md).

## See Also

### Handling marked text
- [func hasMarkedText() -> Bool](./hasmarkedtext%28%29.md)
  Returns a Boolean value indicating whether the receiver has marked text.
- [func selectedRange() -> NSRange](./selectedrange%28%29.md)
  Returns the range of selected text.
- [func setMarkedText(Any, selectedRange: NSRange, replacementRange: NSRange)](./setmarkedtext%28_,selectedrange,replacementrange%29.md)
  Replaces a specified range in the receiver’s text storage with the given string and sets the selection.
- [func unmarkText()](./unmarktext%28%29.md)
  Unmarks the marked text.
- [func validAttributesForMarkedText() -> [NSAttributedString.Key]](./validattributesformarkedtext%28%29.md)
  Returns an array of attribute names recognized by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/markedrange())*