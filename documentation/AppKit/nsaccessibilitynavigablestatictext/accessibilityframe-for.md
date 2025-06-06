# accessibilityFrame(for:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the rectangle that encloses the specified range of characters.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityFrame(for range: NSRange) -> NSRect
```

#### Return Value

The rectangle that encloses the specified characters.

#### Discussion

If the range crosses a line boundary, the returned rectangle will fully enclose all the lines of characters.

## Parameters

- `range`: The range of characters.

## See Also

- [func accessibilityLine(for: Int) -> Int](nsaccessibilitynavigablestatictext/accessibilityline(for:).md)
  Returns the line number for the line that contains the specified character index.
- [func accessibilityRange(forLine: Int) -> NSRange](nsaccessibilitynavigablestatictext/accessibilityrange(forline:).md)
  Returns the range of characters in the specified line.
- [func accessibilityString(for: NSRange) -> String?](nsaccessibilitynavigablestatictext/accessibilitystring(for:).md)
  Returns the substring for the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitynavigablestatictext/accessibilityframe(for:))*