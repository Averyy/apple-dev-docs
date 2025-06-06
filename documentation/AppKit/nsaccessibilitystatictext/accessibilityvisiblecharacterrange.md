# accessibilityVisibleCharacterRange()

**Framework**: AppKit  
**Kind**: method

Returns the range of visible characters in the document.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func accessibilityVisibleCharacterRange() -> NSRange
```

#### Return Value

The range of the visible characters in the document. This method should return the range for entire lines. Characters that are horizontally clipped are included in this range.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilityVisibleCharacterRange`](nsaccessibility-c.protocol/accessibilityvisiblecharacterrange.md) property.

## See Also

- [func accessibilityAttributedString(for: NSRange) -> NSAttributedString?](nsaccessibilitystatictext/accessibilityattributedstring(for:).md)
  Returns the attributed substring for the specified range of characters.
- [func accessibilityValue() -> String?](nsaccessibilitystatictext/accessibilityvalue.md)
  Returns the text that the accessibility element displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitystatictext/accessibilityvisiblecharacterrange())*