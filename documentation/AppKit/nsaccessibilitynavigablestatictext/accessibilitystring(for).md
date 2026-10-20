# accessibilityString(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the substring for the specified range.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityString(for range: NSRange) -> String?
```

```objc
- (NSString *) accessibilityStringForRange:(NSRange) range;
```

#### Return Value

The substring specified by the given range.

## Parameters

- `range`: A range of characters contained by this element.

## See Also

### Supporting Accessibility
- [func accessibilityFrame(for: NSRange) -> NSRect](./accessibilityframe%28for%29.md)
  Returns the rectangle that encloses the specified range of characters.
- [func accessibilityLine(for: Int) -> Int](./accessibilityline%28for%29.md)
  Returns the line number for the line that contains the specified character index.
- [func accessibilityRange(forLine: Int) -> NSRange](./accessibilityrange%28forline%29.md)
  Returns the range of characters in the specified line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitynavigablestatictext/accessibilitystring(for:))*