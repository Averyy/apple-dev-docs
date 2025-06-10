# previous()

**Framework**: Swift  
**Kind**: method

Decode and return the scalar ending at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the start of the returned scalar, which is also the end of the previous scalar.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
mutating func previous() -> Unicode.Scalar?
```

#### Discussion

Returns `nil` if at the start of the `UTF8Span`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/previous())*