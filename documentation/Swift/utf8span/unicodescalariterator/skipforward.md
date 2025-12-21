# skipForward()

**Framework**: Swift  
**Kind**: method

Advance `codeUnitOffset` to the end of the current scalar, without decoding it.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
mutating func skipForward() -> Int
```

#### Discussion

Returns the number of `Unicode.Scalar`s skipped over, which can be 0 if at the end of the UTF8Span.

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/skipforward())*