# accessibilityLine(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the line number for the line that contains the specified character index.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityLine(for index: Int) -> Int
```

```objc
- (NSInteger) accessibilityLineForIndex:(NSInteger) index;
```

#### Return Value

The line number for the line holding the specified character index.

## Parameters

- `index`: The index for a character.

## See Also

### Supporting Accessibility
- [func accessibilityFrame(for: NSRange) -> NSRect](./accessibilityframe%28for%29.md)
  Returns the rectangle that encloses the specified range of characters.
- [func accessibilityRange(forLine: Int) -> NSRange](./accessibilityrange%28forline%29.md)
  Returns the range of characters in the specified line.
- [func accessibilityString(for: NSRange) -> String?](./accessibilitystring%28for%29.md)
  Returns the substring for the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitynavigablestatictext/accessibilityline(for:))*