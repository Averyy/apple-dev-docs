# geometryDescriptors

**Framework**: Metal  
**Kind**: property

Associates the array of geometry descriptors that comprise this primitive acceleration structure.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var geometryDescriptors: [MTL4AccelerationStructureGeometryDescriptor]? { get set }
```

#### Discussion

If you enable keyframe motion by setting property [`motionKeyframeCount`](mtl4primitiveaccelerationstructuredescriptor/motionkeyframecount.md) to a value greater than `1`, then all geometry descriptors this array references need to be motion geometry descriptors and have a number of primitive buffers equals to [`motionKeyframeCount`](mtl4primitiveaccelerationstructuredescriptor/motionkeyframecount.md).

Example of motion geometry descriptors include: [`MTL4AccelerationStructureMotionTriangleGeometryDescriptor`](mtl4accelerationstructuremotiontrianglegeometrydescriptor.md), [`MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor`](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md), [`MTL4AccelerationStructureMotionCurveGeometryDescriptor`](mtl4accelerationstructuremotioncurvegeometrydescriptor.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4primitiveaccelerationstructuredescriptor/geometrydescriptors)*