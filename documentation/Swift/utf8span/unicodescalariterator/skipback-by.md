# skipBack(by:)

**Framework**: Swift  
**Kind**: method

Move `codeUnitOffset` to the start of the previous `n` scalars, without decoding them.

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
mutating func skipBack(by n: Int) -> Int
```

#### Discussion

Returns the number of `Unicode.Scalar`s skipped over, which can be fewer than `n` if at the start of the UTF8Span.

> **Note**: O(n)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/skipback(by:))*