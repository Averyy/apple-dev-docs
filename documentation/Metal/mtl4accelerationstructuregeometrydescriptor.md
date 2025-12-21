# MTL4AccelerationStructureGeometryDescriptor

**Framework**: Metal  
**Kind**: class

Base class for all Metal 4 acceleration structure geometry descriptors.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class MTL4AccelerationStructureGeometryDescriptor
```

#### Overview

Don’t use this class directly. Use one of the derived classes instead.

## Topics

### Instance Properties
- [var allowDuplicateIntersectionFunctionInvocation: Bool](mtl4accelerationstructuregeometrydescriptor/allowduplicateintersectionfunctioninvocation.md)
  A boolean value that indicates whether the ray-tracing system in Metal allows the invocation of intersection functions more than once per ray-primitive intersection.
- [var intersectionFunctionTableOffset: Int](mtl4accelerationstructuregeometrydescriptor/intersectionfunctiontableoffset.md)
  Sets the offset that this geometry contributes to determining the intersection function to invoke when a ray intersects it.
- [var label: String?](mtl4accelerationstructuregeometrydescriptor/label.md)
  Assigns an optional label you can assign to this geometry for debugging purposes.
- [var opaque: Bool](mtl4accelerationstructuregeometrydescriptor/opaque.md)
  Provides a hint to Metal that this geometry is opaque, potentially accelerating the ray/primitive intersection process.
- [var primitiveDataBuffer: MTL4BufferRange](mtl4accelerationstructuregeometrydescriptor/primitivedatabuffer.md)
  Assigns optional buffer containing data to associate with each primitive in this geometry.
- [var primitiveDataElementSize: Int](mtl4accelerationstructuregeometrydescriptor/primitivedataelementsize.md)
  Sets the size, in bytes, of the data for each primitive in the primitive data buffer [`primitiveDataBuffer`](mtl4accelerationstructuregeometrydescriptor/primitivedatabuffer.md) references.
- [var primitiveDataStride: Int](mtl4accelerationstructuregeometrydescriptor/primitivedatastride.md)
  Defines the stride, in bytes, between each primitive’s data in the primitive data buffer [`primitiveDataBuffer`](mtl4accelerationstructuregeometrydescriptor/primitivedatabuffer.md) references.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md)
- [MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md)
- [MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md)
- [MTL4AccelerationStructureMotionCurveGeometryDescriptor](mtl4accelerationstructuremotioncurvegeometrydescriptor.md)
- [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](mtl4accelerationstructuremotiontrianglegeometrydescriptor.md)
- [MTL4AccelerationStructureTriangleGeometryDescriptor](mtl4accelerationstructuretrianglegeometrydescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md)
  A base class for descriptors that contain geometry data to convert into a ray-tracing acceleration structure.
- [class MTL4AccelerationStructureTriangleGeometryDescriptor](mtl4accelerationstructuretrianglegeometrydescriptor.md)
  Describes triangle geometry suitable for ray tracing.
- [class MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md)
  A description of a list of triangle primitives to turn into an acceleration structure.
- [class MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md)
  Describes curve geometry suitable for ray tracing.
- [class MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md)
  A descriptor you configure with curve geometry for building acceleration structures.
- [enum MTLCurveType](mtlcurvetype.md)
- [enum MTLCurveBasis](mtlcurvebasis.md)
- [enum MTLCurveEndCaps](mtlcurveendcaps.md)
- [class MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md)
  Describes bounding-box geometry suitable for ray tracing.
- [class MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md)
  A description of a list of bounding boxes to turn into an acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuregeometrydescriptor)*