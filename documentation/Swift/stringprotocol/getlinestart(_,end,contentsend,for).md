# getLineStart(_:end:contentsEnd:for:)

**Framework**: Swift  
**Kind**: method

Returns by reference the beginning of the first line and the end of the last line touched by the given range.

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
func getLineStart(_ start: UnsafeMutablePointer<Self.Index>, end: UnsafeMutablePointer<Self.Index>, contentsEnd: UnsafeMutablePointer<Self.Index>, for range: some RangeExpression<String.Index>)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/getlinestart(_:end:contentsend:for:))*