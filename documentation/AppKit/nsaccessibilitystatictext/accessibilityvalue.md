# accessibilityValue()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the text that the accessibility element displays.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityValue() -> String?
```

#### Return Value

The text displayed by the element.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilityValue`](nsaccessibility-c.protocol/accessibilityvalue.md) property.

## See Also

- [func accessibilityAttributedString(for: NSRange) -> NSAttributedString?](nsaccessibilitystatictext/accessibilityattributedstring(for:).md)
  Returns the attributed substring for the specified range of characters.
- [func accessibilityVisibleCharacterRange() -> NSRange](nsaccessibilitystatictext/accessibilityvisiblecharacterrange.md)
  Returns the range of visible characters in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitystatictext/accessibilityvalue())*