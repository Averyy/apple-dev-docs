# next()

**Framework**: Swift  
**Kind**: method

Decode and return the scalar starting at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the end of the returned scalar, which is also the start of the next scalar.

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
mutating func next() -> Unicode.Scalar?
```

#### Discussion

Returns `nil` if at the end of the `UTF8Span`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/next())*