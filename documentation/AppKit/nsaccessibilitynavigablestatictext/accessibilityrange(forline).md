# accessibilityRange(forLine:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the range of characters in the specified line.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityRange(forLine lineNumber: Int) -> NSRange
```

```objc
- (NSRange) accessibilityRangeForLine:(NSInteger) lineNumber;
```

## Return Value

The range of characters for the specified line number. If the line ends with a newline character, including the newline is preferred.

## Parameters

- `lineNumber`: The line number to be examined.

## See Also

### Supporting Accessibility
- [func accessibilityFrame(for: NSRange) -> NSRect](./accessibilityframe%28for%29.md)
  Returns the rectangle that encloses the specified range of characters.
- [func accessibilityLine(for: Int) -> Int](./accessibilityline%28for%29.md)
  Returns the line number for the line that contains the specified character index.
- [func accessibilityString(for: NSRange) -> String?](./accessibilitystring%28for%29.md)
  Returns the substring for the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitynavigablestatictext/accessibilityrange(forline:))*