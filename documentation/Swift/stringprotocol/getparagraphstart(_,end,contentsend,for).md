# getParagraphStart(_:end:contentsEnd:for:)

**Framework**: Swift  
**Kind**: method

Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func getParagraphStart(_ start: UnsafeMutablePointer<Self.Index>, end: UnsafeMutablePointer<Self.Index>, contentsEnd: UnsafeMutablePointer<Self.Index>, for range: some RangeExpression<String.Index>)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/getparagraphstart(_:end:contentsend:for:))*