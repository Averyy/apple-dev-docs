# previous()

**Framework**: Swift  
**Kind**: method

Decode and return the scalar ending at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the start of the returned scalar, which is also the end of the previous scalar.

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
mutating func previous() -> Unicode.Scalar?
```

#### Discussion

Returns `nil` if at the start of the `UTF8Span`.

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/previous())*