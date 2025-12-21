# init(options:mask:intersectionFunctionTableOffset:accelerationStructureIndex:userID:motionTransformsStartIndex:motionTransformsCount:motionStartBorderMode:motionEndBorderMode:motionStartTime:motionEndTime:)

**Framework**: Metal  
**Kind**: init

Creates an acceleration-structure motion instance with the property values you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(options: MTLAccelerationStructureInstanceOptions, mask: UInt32, intersectionFunctionTableOffset: UInt32, accelerationStructureIndex: UInt32, userID: UInt32, motionTransformsStartIndex: UInt32, motionTransformsCount: UInt32, motionStartBorderMode: MTLMotionBorderMode, motionEndBorderMode: MTLMotionBorderMode, motionStartTime: Float, motionEndTime: Float)
```

#### Discussion

The initializer sets the descriptor instance’s properties to the values you pass to the initializer’s parameters. However, you can change the descriptor’s property values at any time, such as between creating separate acceleration-structure motion instances. For example, apps typically assign a unique value to [`userID`](mtlaccelerationstructuremotioninstancedescriptor/userid.md) before they create each motion instance with the same descriptor.

## Parameters

- `options`: An option set for new acceleration-structure motion instances.
- `mask`: A mask for testing ray-tracing rays in a scene’s geometry   for new acceleration-structure motion-instances.
- `intersectionFunctionTableOffset`: An offset into the intersection-function   table for ray tracing.
- `accelerationStructureIndex`: The index of an acceleration structure   that applies to new acceleration-structure motion-instances.
- `userID`: An unique identifier for an acceleration-structure motion-instance.
- `motionTransformsStartIndex`: An index of the motion data that represents the first   key-frame’s motion data.
- `motionTransformsCount`: The number of motion data key-frames that begin at   .
- `motionStartBorderMode`: A behavior that configures how an acceleration-structure   motion-instance handles timestamps before  .
- `motionEndBorderMode`: A behavior that configures how an acceleration-structure   motion-instance handles timestamps after  .
- `motionStartTime`: A starting time for the range of motion that the key-frame data   (see   and  ) represent.
- `motionEndTime`: An ending time for the range of motion that the key-frame data   (see   and  ) represent.

## See Also

- [init()](mtlaccelerationstructuremotioninstancedescriptor/init.md)
  Creates an acceleration-structure motion instance with default property values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/init(options:mask:intersectionfunctiontableoffset:accelerationstructureindex:userid:motiontransformsstartindex:motiontransformscount:motionstartbordermode:motionendbordermode:motionstarttime:motionendtime:))*