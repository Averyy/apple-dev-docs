# MTLAccelerationStructureBoundingBoxGeometryDescriptor

**Framework**: Metal  
**Kind**: class

A description of a list of bounding boxes to turn into an acceleration structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLAccelerationStructureBoundingBoxGeometryDescriptor
```

## Mentions

- [Improving Ray-Tracing Data Access Using Per-Primitive Data](improving-ray-tracing-data-access-using-per-primitive-data.md)

## Topics

### Specifying the Number of Bounding Boxes
- [var boundingBoxCount: Int](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxcount.md)
  The number of bounding boxes in the bounding box buffer.
### Specifying Bounding Boxes Data
- [var boundingBoxBuffer: (any MTLBuffer)?](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbuffer.md)
  A buffer that contains bounding box data.
- [var boundingBoxBufferOffset: Int](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbufferoffset.md)
  The offset, in bytes, to the first bounding box in the buffer.
- [var boundingBoxStride: Int](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxstride.md)
  The stride, in bytes, between bounding boxes in the buffer.

## Relationships

### Inherits From
- [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md)
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
- [class MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md)
  A description of a list of triangle primitives to turn into an acceleration structure.
- [class MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md)
- [enum MTLCurveType](mtlcurvetype.md)
- [enum MTLCurveBasis](mtlcurvebasis.md)
- [enum MTLCurveEndCaps](mtlcurveendcaps.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor)*