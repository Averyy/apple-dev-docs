# skipBack()

**Framework**: Swift  
**Kind**: method

Move `codeUnitOffset` to the start of the previous scalar, without decoding it.

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
mutating func skipBack() -> Int
```

#### Discussion

Returns the number of `Unicode.Scalar`s skipped over, which can be 0 if at the start of the UTF8Span.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/skipback())*