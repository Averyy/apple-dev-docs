# MPSGraphResizeMode

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MPSGraphResizeMode : NSUInteger;
```

## Topics

### Enumeration Cases
- [MPSGraphResizeMode.bilinear](./mpsgraphresizemode/bilinear.md)
  Samples the 4 neighbors to the pixel coordinate and uses bilinear interpolation.
- [MPSGraphResizeMode.nearest](./mpsgraphresizemode/nearest.md)
  Samples the nearest neighbor to the pixel coordinate.
### Initializers
- [init?(rawValue: UInt)](./mpsgraphresizemode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphresizemode)*