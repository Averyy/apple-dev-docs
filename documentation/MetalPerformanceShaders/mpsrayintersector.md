# MPSRayIntersector

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A kernel that performs intersection tests between rays and geometry.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.14+ - Deprecated in 14.0
- tvOS 12.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class MPSRayIntersector
```

```objc
@interface MPSRayIntersector : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsrayintersector/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsrayintersector/init%28device%29.md)
### Instance Properties
- [var boundingBoxIntersectionTestType: MPSBoundingBoxIntersectionTestType](./mpsrayintersector/boundingboxintersectiontesttype.md)
- [var cullMode: MTLCullMode](./mpsrayintersector/cullmode.md)
- [var frontFacingWinding: MTLWinding](./mpsrayintersector/frontfacingwinding.md)
- [var intersectionDataType: MPSIntersectionDataType](./mpsrayintersector/intersectiondatatype.md)
- [var intersectionStride: Int](./mpsrayintersector/intersectionstride.md)
- [var rayDataType: MPSRayDataType](./mpsrayintersector/raydatatype.md)
- [var rayIndexDataType: MPSDataType](./mpsrayintersector/rayindexdatatype.md)
- [var rayMask: UInt32](./mpsrayintersector/raymask.md)
- [var rayMaskOperator: MPSRayMaskOperator](./mpsrayintersector/raymaskoperator.md)
- [var rayMaskOptions: MPSRayMaskOptions](./mpsrayintersector/raymaskoptions.md)
- [var rayStride: Int](./mpsrayintersector/raystride.md)
- [var triangleIntersectionTestType: MPSTriangleIntersectionTestType](./mpsrayintersector/triangleintersectiontesttype.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsrayintersector/copy%28with,device%29.md)
- [func encode(with: NSCoder)](./mpsrayintersector/encode%28with%29.md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayBuffer: any MTLBuffer, rayBufferOffset: Int, intersectionBuffer: any MTLBuffer, intersectionBufferOffset: Int, rayCount: Int, accelerationStructure: MPSAccelerationStructure)](./mpsrayintersector/encodeintersection%28commandbuffer,intersectiontype,raybuffer,raybufferoffset,intersectionbuffer,intersectionbufferoffset,raycount,accelerationstructure%29.md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayBuffer: any MTLBuffer, rayBufferOffset: Int, intersectionBuffer: any MTLBuffer, intersectionBufferOffset: Int, rayCountBuffer: any MTLBuffer, rayCountBufferOffset: Int, accelerationStructure: MPSAccelerationStructure)](./mpsrayintersector/encodeintersection%28commandbuffer,intersectiontype,raybuffer,raybufferoffset,intersectionbuffer,intersectionbufferoffset,raycountbuffer,raycountbufferoffset,accelerationstructure%29.md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayBuffer: any MTLBuffer, rayBufferOffset: Int, rayIndexBuffer: any MTLBuffer, rayIndexBufferOffset: Int, intersectionBuffer: any MTLBuffer, intersectionBufferOffset: Int, rayIndexCount: Int, accelerationStructure: MPSAccelerationStructure)](./mpsrayintersector/encodeintersection%28commandbuffer,intersectiontype,raybuffer,raybufferoffset,rayindexbuffer,rayindexbufferoffset,intersectionbuffer,intersectionbufferoffset,rayindexcount,accelerationstructure%29.md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayBuffer: any MTLBuffer, rayBufferOffset: Int, rayIndexBuffer: any MTLBuffer, rayIndexBufferOffset: Int, intersectionBuffer: any MTLBuffer, intersectionBufferOffset: Int, rayIndexCountBuffer: any MTLBuffer, rayIndexCountBufferOffset: Int, accelerationStructure: MPSAccelerationStructure)](./mpsrayintersector/encodeintersection%28commandbuffer,intersectiontype,raybuffer,raybufferoffset,rayindexbuffer,rayindexbufferoffset,intersectionbuffer,intersectionbufferoffset,rayindexcountbuffer,rayindexcountbufferoffset,accelerationstructure%29.md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayTexture: any MTLTexture, intersectionTexture: any MTLTexture, accelerationStructure: MPSAccelerationStructure)](./mpsrayintersector/encodeintersection%28commandbuffer,intersectiontype,raytexture,intersectiontexture,accelerationstructure%29.md)
- [func recommendedMinimumRayBatchSize(rayCount: Int) -> Int](./mpsrayintersector/recommendedminimumraybatchsize%28raycount%29.md)

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
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
- [class MPSAccelerationStructureGroup](./mpsaccelerationstructuregroup.md)
  A group of acceleration structures.
- [class MPSInstanceAccelerationStructure](./mpsinstanceaccelerationstructure.md)
  An acceleration structure built over instances of other acceleration structures.
- [class MPSTriangleAccelerationStructure](./mpstriangleaccelerationstructure.md)
  An acceleration structure built over triangles.
- [class MPSAccelerationStructure](./mpsaccelerationstructure.md)
  The base class for data structures that are built over geometry and used to accelerate ray tracing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrayintersector)*