# LowLevelRenderer.CullConfiguration.Plane

**Framework**: RealityKit  
**Kind**: struct

An infinite directed plane used to cull mesh instances.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@frozen
struct Plane
```

#### Overview

Each plane has an outward normal that points away from the visible region. An instance is culled when its mesh part bounds lie entirely on the outward side of the plane.

## Topics

### Creating a plane
- [init(position: SIMD3<Float>, direction: SIMD3<Float>)](lowlevelrenderer/cullconfiguration/plane/init(position:direction:).md)
  Creates a plane from a point on the plane and an outward normal direction.
- [init(position0: SIMD3<Float>, position1: SIMD3<Float>, position2: SIMD3<Float>)](lowlevelrenderer/cullconfiguration/plane/init(position0:position1:position2:).md)
  Creates a plane from three positions.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cullconfiguration/plane)*