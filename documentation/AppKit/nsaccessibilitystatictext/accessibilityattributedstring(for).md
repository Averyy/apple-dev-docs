# accessibilityAttributedString(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the attributed substring for the specified range of characters.

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func accessibilityAttributedString(for range: NSRange) -> NSAttributedString?
```

```objc
- (NSAttributedString *) accessibilityAttributedStringForRange:(NSRange) range;
```

#### Return Value

An attributed string representing the specified characters.

## Parameters

- `range`: The range of characters.

## See Also

### Supporting Accessibility
- [func accessibilityValue() -> String?](./accessibilityvalue%28%29.md)
  Returns the text that the accessibility element displays.
- [func accessibilityVisibleCharacterRange() -> NSRange](./accessibilityvisiblecharacterrange%28%29.md)
  Returns the range of visible characters in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitystatictext/accessibilityattributedstring(for:))*