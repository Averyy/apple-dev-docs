# accessibilityVisibleCharacterRange()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the range of visible characters in the document.

**Availability**:
- macOS

## Declaration

```swift
optional func accessibilityVisibleCharacterRange() -> NSRange
```

```objc
- (NSRange) accessibilityVisibleCharacterRange;
```

#### Return Value

The range of the visible characters in the document. This method should return the range for entire lines. Characters that are horizontally clipped are included in this range.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilityVisibleCharacterRange`](../nsaccessibility-c.protocol/accessibilityvisiblecharacterrange.md) property.

## See Also

### Supporting Accessibility
- [func accessibilityAttributedString(for: NSRange) -> NSAttributedString?](./accessibilityattributedstring%28for%29.md)
  Returns the attributed substring for the specified range of characters.
- [func accessibilityValue() -> String?](./accessibilityvalue%28%29.md)
  Returns the text that the accessibility element displays.
### Related Documentation
- [accessibilityVisibleCharacterRange](../nsaccessibility-c.protocol/accessibilityvisiblecharacterrange.md)
  The range of visible characters in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitystatictext/accessibilityvisiblecharacterrange())*