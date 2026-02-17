# utf8Span

**Framework**: Swift  
**Kind**: property

A UTF-8 span over the code units that make up this string.

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
var utf8Span: UTF8Span { get }
```

#### Return Value

A `UTF8Span` over the code units of this string.

#### Discussion

> **Note**: In the case of bridged UTF-16 string instances (on Apple platforms) this property transcodes the code units the first time it’s called. The transcoded buffer is cached, and subsequent calls can reuse the buffer.

> **Note**: O(1) for native UTF-8 strings, amortized O(1) for bridged UTF-16 strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/utf8span)*