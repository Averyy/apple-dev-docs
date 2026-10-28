# geometryDescriptors

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

An array that contains the individual pieces of geometry that compose the acceleration structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var geometryDescriptors: [MTLAccelerationStructureGeometryDescriptor]? { get set }
```

```objc
@property (nonatomic, retain, nullable) NSArray<MTLAccelerationStructureGeometryDescriptor *> * geometryDescriptors;
```

## Discussion

The value of the [`motionKeyframeCount`](./motionkeyframecount.md) property determines what kinds of geometry descriptors you can assign to this property and how you need to configure them.

If the value of [`motionKeyframeCount`](./motionkeyframecount.md) is greater than 1, then the geometry descriptors need to be either [`MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor`](../mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md) or [`MTLAccelerationStructureMotionTriangleGeometryDescriptor`](../mtlaccelerationstructuremotiontrianglegeometrydescriptor.md) objects. Further, you need to provide exactly that many keyframes of data when creating those geometry descriptors. If [`motionKeyframeCount`](./motionkeyframecount.md)  is 1, use [`MTLAccelerationStructureBoundingBoxGeometryDescriptor`](../mtlaccelerationstructureboundingboxgeometrydescriptor.md) or [`MTLAccelerationStructureTriangleGeometryDescriptor`](../mtlaccelerationstructuretrianglegeometrydescriptor.md) objects instead.

## See Also

### Related Documentation
- [var motionKeyframeCount: Int](./motionkeyframecount.md)
  The number of keyframes in the geometry data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlprimitiveaccelerationstructuredescriptor/geometrydescriptors)*