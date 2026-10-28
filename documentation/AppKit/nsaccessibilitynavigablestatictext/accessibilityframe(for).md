# accessibilityFrame(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the rectangle that encloses the specified range of characters.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityFrame(for range: NSRange) -> NSRect
```

```objc
- (NSRect) accessibilityFrameForRange:(NSRange) range;
```

## Return Value

The rectangle that encloses the specified characters.

## Discussion

If the range crosses a line boundary, the returned rectangle will fully enclose all the lines of characters.

## Parameters

- `range`: The range of characters.

## See Also

### Supporting Accessibility
- [func accessibilityLine(for: Int) -> Int](./accessibilityline%28for%29.md)
  Returns the line number for the line that contains the specified character index.
- [func accessibilityRange(forLine: Int) -> NSRange](./accessibilityrange%28forline%29.md)
  Returns the range of characters in the specified line.
- [func accessibilityString(for: NSRange) -> String?](./accessibilitystring%28for%29.md)
  Returns the substring for the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitynavigablestatictext/accessibilityframe(for:))*