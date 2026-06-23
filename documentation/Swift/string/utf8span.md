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

A `UTF8Span` over the code units of this `String`.

#### Discussion

> **Note**: On Apple platforms, this property transcodes the code units of bridged UTF-16 `String` instances on first access and caches the result. Subsequent calls can reuse the cached buffer.

> **Note**: O(1) for native UTF-8 strings, amortized O(1) for bridged UTF-16 strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/utf8span)*