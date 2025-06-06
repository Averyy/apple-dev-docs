# MTLAccelerationStructureGeometryDescriptor

**Framework**: Metal  
**Kind**: class

A base class for descriptors that contain geometry data to convert into a ray-tracing acceleration structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLAccelerationStructureGeometryDescriptor
```

## Mentions

- [Improving Ray-Tracing Data Access Using Per-Primitive Data](improving-ray-tracing-data-access-using-per-primitive-data.md)

#### Overview

Don’t use this base class directly. Use one of the derived classes instead, as  [`MTLAccelerationStructure`](mtlaccelerationstructure.md) describes.

## Topics

### Specifying Base Geometry Properties
- [var label: String?](mtlaccelerationstructuregeometrydescriptor/label.md)
  A label for the geometry structure, suitable for debugging.
- [var intersectionFunctionTableOffset: Int](mtlaccelerationstructuregeometrydescriptor/intersectionfunctiontableoffset.md)
  An index into the intersection table for determining which intersection function Metal calls when it intersects a ray with the acceleration structure.
- [var opaque: Bool](mtlaccelerationstructuregeometrydescriptor/opaque.md)
  A Boolean value that determines whether the geometry data in the acceleration structure needs to skip triangle-intersection tests.
- [var allowDuplicateIntersectionFunctionInvocation: Bool](mtlaccelerationstructuregeometrydescriptor/allowduplicateintersectionfunctioninvocation.md)
  A Boolean value that indicates whether Metal calls the ray-intersection test more than once per primitive on the structure.
### Instance Properties
- [var primitiveDataBuffer: (any MTLBuffer)?](mtlaccelerationstructuregeometrydescriptor/primitivedatabuffer.md)
- [var primitiveDataBufferOffset: Int](mtlaccelerationstructuregeometrydescriptor/primitivedatabufferoffset.md)
- [var primitiveDataElementSize: Int](mtlaccelerationstructuregeometrydescriptor/primitivedataelementsize.md)
- [var primitiveDataStride: Int](mtlaccelerationstructuregeometrydescriptor/primitivedatastride.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md)
- [MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md)
- [MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md)
- [MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md)
- [MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md)
  A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.
- [class MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md)
  A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.
- [class MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md)
  A description of a list of triangle primitives to turn into an acceleration structure.
- [class MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md)
- [enum MTLCurveType](mtlcurvetype.md)
- [enum MTLCurveBasis](mtlcurvebasis.md)
- [enum MTLCurveEndCaps](mtlcurveendcaps.md)
- [class MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md)
  A description of a list of bounding boxes to turn into an acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuregeometrydescriptor)*