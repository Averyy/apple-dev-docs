# accessibilityLine(for:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the line number for the line that contains the specified character index.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityLine(for index: Int) -> Int
```

#### Return Value

The line number for the line holding the specified character index.

## Parameters

- `index`: The index for a character.

## See Also

- [func accessibilityFrame(for: NSRange) -> NSRect](nsaccessibilitynavigablestatictext/accessibilityframe(for:).md)
  Returns the rectangle that encloses the specified range of characters.
- [func accessibilityRange(forLine: Int) -> NSRange](nsaccessibilitynavigablestatictext/accessibilityrange(forline:).md)
  Returns the range of characters in the specified line.
- [func accessibilityString(for: NSRange) -> String?](nsaccessibilitynavigablestatictext/accessibilitystring(for:).md)
  Returns the substring for the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitynavigablestatictext/accessibilityline(for:))*