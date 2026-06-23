# span

**Framework**: Swift  
**Kind**: property

A span over the elements of this buffer.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
var span: Span<Element> { get }
```

#### Return Value

A `Span` over the elements of this buffer.

#### Discussion

The lifetime of the returned span matches the lifetime of the binding which returns it. This lifetime is a convenience, as there can be no enforcement that there is no concurrent write to the underlying memory. The programmer must ensure that the memory remains allocated, initialized and immutable for the lifetime of the returned span.

> **Note**: This property is unsafe because it cannot guarantee that the underlying memory remains valid and immutable for the lifetime of the returned span.

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/span)*