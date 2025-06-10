# MPSGraphResizeMode

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum

The resize mode to use for resizing.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphResizeMode
```

## Topics

### Enumeration Cases
- [MPSGraphResizeMode.bilinear](mpsgraphresizemode/bilinear.md)
  Samples the 4 neighbors to the pixel coordinate and uses bilinear interpolation.
- [MPSGraphResizeMode.nearest](mpsgraphresizemode/nearest.md)
  Samples the nearest neighbor to the pixel coordinate.
### Initializers
- [init?(rawValue: UInt)](mpsgraphresizemode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphresizemode)*