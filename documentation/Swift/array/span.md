# span

**Framework**: Swift  
**Kind**: property

A span over the elements of this array.

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
var span: Span<Element> { get }
```

#### Return Value

A `Span` over the elements of this array.

#### Discussion

> **Note**: On Apple platforms, this property copies bridged `NSArray` instances into contiguous storage on first access and caches the result. Subsequent calls can reuse the cached copy.

> **Note**: O(1) for native arrays, amortized O(1) for bridged arrays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/span)*