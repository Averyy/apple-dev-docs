# init(transformationMatrix:options:mask:intersectionFunctionTableOffset:accelerationStructureIndex:userID:)

**Framework**: Metal  
**Kind**: init

Creates a new acceleration structure instance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(transformationMatrix: MTLPackedFloat4x3, options: MTLAccelerationStructureInstanceOptions, mask: UInt32, intersectionFunctionTableOffset: UInt32, accelerationStructureIndex: UInt32, userID: UInt32)
```

## Parameters

- `transformationMatrix`: The transform for placing and orienting the instance in the scene.
- `options`: The options for the instance.
- `mask`: A mask to use for the instance when testing a ray against the geometry.
- `intersectionFunctionTableOffset`: An offset to apply to the intersection function table when testing a ray against the instance.
- `accelerationStructureIndex`: The index of the acceleration structure to use for the instance.
- `userID`: The user identifier for the instance.

## See Also

- [init()](mtlaccelerationstructureuseridinstancedescriptor/init.md)
  Creates a default acceleration structure instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/init(transformationmatrix:options:mask:intersectionfunctiontableoffset:accelerationstructureindex:userid:))*