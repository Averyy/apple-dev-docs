# accessibilityRTF(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the rich text format (RTF) data that describes the specified range of characters.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityRTF(for range: NSRange) -> Data?
```

```objc
- (NSData *) accessibilityRTFForRange:(NSRange) range;
```

## Return Value

A data object containing an RTF representation of the specified characters.

## Parameters

- `range`: The range of characters.

## See Also

### Configuring text elements
- [func accessibilityInsertionPointLineNumber() -> Int](./accessibilityinsertionpointlinenumber%28%29.md)
  Returns the line number that contains the insertion point.
- [func setAccessibilityInsertionPointLineNumber(Int)](./setaccessibilityinsertionpointlinenumber%28_%29.md)
  Sets the line number that contains the insertion point.
- [func accessibilityNumberOfCharacters() -> Int](./accessibilitynumberofcharacters%28%29.md)
  Returns the number of characters in the text.
- [func setAccessibilityNumberOfCharacters(Int)](./setaccessibilitynumberofcharacters%28_%29.md)
  Sets the number of characters in the text.
- [func accessibilityPlaceholderValue() -> String?](./accessibilityplaceholdervalue%28%29.md)
  Returns the placeholder value for the accessibility element.
- [func setAccessibilityPlaceholderValue(String?)](./setaccessibilityplaceholdervalue%28_%29.md)
  Sets the placeholder value for the accessibility element.
- [func accessibilitySelectedText() -> String?](./accessibilityselectedtext%28%29.md)
  Returns the currently selected text.
- [func setAccessibilitySelectedText(String?)](./setaccessibilityselectedtext%28_%29.md)
  Sets the currently selected text.
- [func accessibilitySelectedTextRange() -> NSRange](./accessibilityselectedtextrange%28%29.md)
  Returns the range of the currently selected text.
- [func setAccessibilitySelectedTextRange(NSRange)](./setaccessibilityselectedtextrange%28_%29.md)
  Sets the range of the currently selected text.
- [func accessibilitySelectedTextRanges() -> [NSValue]?](./accessibilityselectedtextranges%28%29.md)
  Returns an array of ranges for the currently selected text.
- [func setAccessibilitySelectedTextRanges([NSValue]?)](./setaccessibilityselectedtextranges%28_%29.md)
  Sets an array of ranges for the currently selected text.
- [func accessibilitySharedCharacterRange() -> NSRange](./accessibilitysharedcharacterrange%28%29.md)
  Returns the range of characters that the accessibility element displays.
- [func setAccessibilitySharedCharacterRange(NSRange)](./setaccessibilitysharedcharacterrange%28_%29.md)
  Sets the range of characters that the accessibility element displays.
- [func accessibilitySharedTextUIElements() -> [Any]?](./accessibilitysharedtextuielements%28%29.md)
  Returns the other elements that share text with the accessibility element.
- [- accessibilityStringForRange:](./accessibilitystring%28for%29.md)
  Returns the substring for the specified range.
- [- accessibilityAttributedStringForRange:](./accessibilityattributedstring%28for%29.md)
  Returns the attributed substring for the specified range of characters.
- [- accessibilityFrameForRange:](./accessibilityframe%28for%29.md)
  Returns the rectangle that encloses the specified range of characters.
- [- accessibilityLineForIndex:](./accessibilityline%28for%29.md)
  Returns the line number for the line that contains the specified character index.
- [- accessibilityRangeForIndex:](./accessibilityrange%28for%29-6kv3.md)
  Returns the range of characters for the glyph that includes the specified character.
- [- accessibilityStyleRangeForIndex:](./accessibilitystylerange%28for%29.md)
  Returns a range of characters that all have the same style as the specified character.
- [- accessibilityRangeForLine:](./accessibilityrange%28forline%29.md)
  Returns the range of characters in the specified line.
- [- accessibilityRangeForPosition:](./accessibilityrange%28for%29-1iudm.md)
  Returns the range of characters for the glyph at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityrtf(for:))*