# hasMarkedText()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns a Boolean value indicating whether the receiver has marked text.

**Availability**:
- macOS ?+

## Declaration

```swift
func hasMarkedText() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver has marked text; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The text view itself may call this method to determine whether there currently is marked text. `NSTextView`, for example, disables the Edit > Copy menu item when this method returns [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func markedRange() -> NSRange](nstextinputclient/markedrange.md)
  Returns the range of the marked text.
- [func selectedRange() -> NSRange](nstextinputclient/selectedrange.md)
  Returns the range of selected text.
- [func setMarkedText(Any, selectedRange: NSRange, replacementRange: NSRange)](nstextinputclient/setmarkedtext(_:selectedrange:replacementrange:).md)
  Replaces a specified range in the receiver’s text storage with the given string and sets the selection.
- [func unmarkText()](nstextinputclient/unmarktext.md)
  Unmarks the marked text.
- [func validAttributesForMarkedText() -> [NSAttributedString.Key]](nstextinputclient/validattributesformarkedtext.md)
  Returns an array of attribute names recognized by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/hasmarkedtext())*