# span

**Framework**: Swift  
**Kind**: property

A span over the UTF8 code units that make up this string.

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
var span: Span<UTF8.CodeUnit> { get }
```

#### Discussion

> **Note**: In the case of bridged UTF16 String instances (on Apple platforms,) this property transcodes the code units the first time it is called. The transcoded buffer is cached, and subsequent calls to `span` can reuse the buffer.

Returns: a `Span` over the UTF8 code units of this String.

Complexity: O(1) for native UTF8 Strings, amortized O(1) for bridged UTF16 Strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/utf8view/span)*