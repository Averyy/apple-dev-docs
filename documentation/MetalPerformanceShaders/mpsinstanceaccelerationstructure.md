# MPSInstanceAccelerationStructure

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

An acceleration structure built over instances of other acceleration structures.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.14+ - Deprecated in 14.0
- tvOS 12.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class MPSInstanceAccelerationStructure
```

```objc
@interface MPSInstanceAccelerationStructure : MPSAccelerationStructure
```

## Topics

### Instance Properties
- [var accelerationStructures: [MPSPolygonAccelerationStructure]?](./mpsinstanceaccelerationstructure/accelerationstructures.md)
- [var instanceBuffer: (any MTLBuffer)?](./mpsinstanceaccelerationstructure/instancebuffer.md)
- [var instanceBufferOffset: Int](./mpsinstanceaccelerationstructure/instancebufferoffset.md)
- [var instanceCount: Int](./mpsinstanceaccelerationstructure/instancecount.md)
- [var maskBuffer: (any MTLBuffer)?](./mpsinstanceaccelerationstructure/maskbuffer.md)
- [var maskBufferOffset: Int](./mpsinstanceaccelerationstructure/maskbufferoffset.md)
- [var transformBuffer: (any MTLBuffer)?](./mpsinstanceaccelerationstructure/transformbuffer.md)
- [var transformBufferOffset: Int](./mpsinstanceaccelerationstructure/transformbufferoffset.md)
- [var transformType: MPSTransformType](./mpsinstanceaccelerationstructure/transformtype.md)

## Relationships

### Inherits From
- [MPSAccelerationStructure](./mpsaccelerationstructure.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Ray Tracing
- [Accelerating ray tracing and motion blur using Metal](../Metal/accelerating-ray-tracing-and-motion-blur-using-metal.md)
  Generate ray-traced images with motion blur using GPU-based parallel processing.
- [class MPSRayIntersector](./mpsrayintersector.md)
  A kernel that performs intersection tests between rays and geometry.
- [class MPSAccelerationStructureGroup](./mpsaccelerationstructuregroup.md)
  A group of acceleration structures.
- [class MPSTriangleAccelerationStructure](./mpstriangleaccelerationstructure.md)
  An acceleration structure built over triangles.
- [class MPSAccelerationStructure](./mpsaccelerationstructure.md)
  The base class for data structures that are built over geometry and used to accelerate ray tracing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsinstanceaccelerationstructure)*