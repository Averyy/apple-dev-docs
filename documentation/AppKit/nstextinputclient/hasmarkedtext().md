# hasMarkedText()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value indicating whether the receiver has marked text.

**Availability**:
- macOS

## Declaration

```swift
func hasMarkedText() -> Bool
```

```objc
- (BOOL) hasMarkedText;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver has marked text; otherwise [`false`](../../Swift/false.md).

## Discussion

The text view itself may call this method to determine whether there currently is marked text. `NSTextView`, for example, disables the Edit > Copy menu item when this method returns [`true`](../../Swift/true.md).

## See Also

### Handling marked text
- [func markedRange() -> NSRange](./markedrange%28%29.md)
  Returns the range of the marked text.
- [func selectedRange() -> NSRange](./selectedrange%28%29.md)
  Returns the range of selected text.
- [func setMarkedText(Any, selectedRange: NSRange, replacementRange: NSRange)](./setmarkedtext%28_,selectedrange,replacementrange%29.md)
  Replaces a specified range in the receiver’s text storage with the given string and sets the selection.
- [func unmarkText()](./unmarktext%28%29.md)
  Unmarks the marked text.
- [func validAttributesForMarkedText() -> [NSAttributedString.Key]](./validattributesformarkedtext%28%29.md)
  Returns an array of attribute names recognized by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/hasmarkedtext())*