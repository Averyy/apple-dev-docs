# accessibilityString(for:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the substring for the specified range.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityString(for range: NSRange) -> String?
```

#### Return Value

The substring specified by the given range.

## Parameters

- `range`: A range of characters contained by this element.

## See Also

- [func accessibilityFrame(for: NSRange) -> NSRect](nsaccessibilitynavigablestatictext/accessibilityframe(for:).md)
  Returns the rectangle that encloses the specified range of characters.
- [func accessibilityLine(for: Int) -> Int](nsaccessibilitynavigablestatictext/accessibilityline(for:).md)
  Returns the line number for the line that contains the specified character index.
- [func accessibilityRange(forLine: Int) -> NSRange](nsaccessibilitynavigablestatictext/accessibilityrange(forline:).md)
  Returns the range of characters in the specified line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitynavigablestatictext/accessibilitystring(for:))*