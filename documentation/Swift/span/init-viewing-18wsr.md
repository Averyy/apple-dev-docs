# init(viewing:)

**Framework**: Swift  
**Kind**: init

View initialized raw memory as a typed span.

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
init(viewing bytes: RawSpan) where Element : ConvertibleFromBytes
```

#### Discussion

The `byteCount` of `bytes` must be a multiple of `Element`’s stride, and the starting address of `bytes` must be well-aligned for the type of `Element`. If either of these requirements is not met, this initializer will trap at runtime.

## Parameters

- `bytes`: An existing `RawSpan`, which will define both this `Span`’s lifetime and the memory it represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/span/init(viewing:)-18wsr)*