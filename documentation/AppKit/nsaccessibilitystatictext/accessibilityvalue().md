# accessibilityValue()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the text that the accessibility element displays.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityValue() -> String?
```

```objc
- (NSString *) accessibilityValue;
```

## Return Value

The text displayed by the element.

## Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilityValue`](../nsaccessibility-c.protocol/accessibilityvalue.md) property.

## See Also

### Supporting Accessibility
- [func accessibilityAttributedString(for: NSRange) -> NSAttributedString?](./accessibilityattributedstring%28for%29.md)
  Returns the attributed substring for the specified range of characters.
- [func accessibilityVisibleCharacterRange() -> NSRange](./accessibilityvisiblecharacterrange%28%29.md)
  Returns the range of visible characters in the document.
### Related Documentation
- [accessibilityValue](../nsaccessibility-c.protocol/accessibilityvalue.md)
  The accessibility element’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitystatictext/accessibilityvalue())*