# accessibilityAttributedString(for:)

**Framework**: AppKit  
**Kind**: method

Returns the attributed substring for the specified range of characters.

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func accessibilityAttributedString(for range: NSRange) -> NSAttributedString?
```

#### Return Value

An attributed string representing the specified characters.

## Parameters

- `range`: The range of characters.

## See Also

- [func accessibilityValue() -> String?](nsaccessibilitystatictext/accessibilityvalue.md)
  Returns the text that the accessibility element displays.
- [func accessibilityVisibleCharacterRange() -> NSRange](nsaccessibilitystatictext/accessibilityvisiblecharacterrange.md)
  Returns the range of visible characters in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitystatictext/accessibilityattributedstring(for:))*