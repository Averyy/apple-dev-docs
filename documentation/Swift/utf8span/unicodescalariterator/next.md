# next()

**Framework**: Swift  
**Kind**: method

Decode and return the scalar starting at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the end of the returned scalar, which is also the start of the next scalar.

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
mutating func next() -> Unicode.Scalar?
```

#### Discussion

Returns `nil` if at the end of the `UTF8Span`.

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/next())*