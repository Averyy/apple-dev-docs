# makeUnicodeScalarIterator()

**Framework**: Swift  
**Kind**: method

Returns an iterator that will decode the code units into `Unicode.Scalar`s.

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
func makeUnicodeScalarIterator() -> UTF8Span.UnicodeScalarIterator
```

#### Discussion

The resulting iterator has the same lifetime constraints as `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/makeunicodescalariterator())*