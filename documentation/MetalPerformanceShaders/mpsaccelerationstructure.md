# MPSAccelerationStructure

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

The base class for data structures that are built over geometry and used to accelerate ray tracing.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.14+ - Deprecated in 14.0
- tvOS 12.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class MPSAccelerationStructure
```

```objc
@interface MPSAccelerationStructure : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsaccelerationstructure/init%28coder,device%29.md)
- [init?(coder: NSCoder, group: MPSAccelerationStructureGroup)](./mpsaccelerationstructure/init%28coder,group%29.md)
- [init(device: any MTLDevice)](./mpsaccelerationstructure/init%28device%29.md)
- [init(group: MPSAccelerationStructureGroup)](./mpsaccelerationstructure/init%28group%29.md)
### Instance Properties
- [var boundingBox: MPSAxisAlignedBoundingBox](./mpsaccelerationstructure/boundingbox.md)
- [var group: MPSAccelerationStructureGroup](./mpsaccelerationstructure/group.md)
- [var status: MPSAccelerationStructureStatus](./mpsaccelerationstructure/status.md)
- [var usage: MPSAccelerationStructureUsage](./mpsaccelerationstructure/usage.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsaccelerationstructure/copy%28with,device%29.md)
- [func copy(with: NSZone?, group: MPSAccelerationStructureGroup) -> Self](./mpsaccelerationstructure/copy%28with,group%29.md)
- [func encode(with: NSCoder)](./mpsaccelerationstructure/encode%28with%29.md)
- [func encodeRefit(commandBuffer: any MTLCommandBuffer)](./mpsaccelerationstructure/encoderefit%28commandbuffer%29.md)
- [func rebuild()](./mpsaccelerationstructure/rebuild%28%29.md)
- [func rebuild(completionHandler: (MPSAccelerationStructure?) -> Void)](./mpsaccelerationstructure/rebuild%28completionhandler%29.md)

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
### Inherited By
- [MPSInstanceAccelerationStructure](./mpsinstanceaccelerationstructure.md)
- [MPSPolygonAccelerationStructure](./mpspolygonaccelerationstructure.md)
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
- [class MPSInstanceAccelerationStructure](./mpsinstanceaccelerationstructure.md)
  An acceleration structure built over instances of other acceleration structures.
- [class MPSTriangleAccelerationStructure](./mpstriangleaccelerationstructure.md)
  An acceleration structure built over triangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsaccelerationstructure)*