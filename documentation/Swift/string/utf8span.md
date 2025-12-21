# utf8Span

**Framework**: Swift  
**Kind**: property

A UTF8span over the code units that make up this string.

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

#### Discussion

> **Note**: In the case of bridged UTF16 String instances (on Apple platforms,) this property transcodes the code units the first time it is called. The transcoded buffer is cached, and subsequent calls to `span` can reuse the buffer.

Returns: a `UTF8Span` over the code units of this String.

Complexity: O(1) for native UTF8 Strings, amortized O(1) for bridged UTF16 Strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/utf8span)*