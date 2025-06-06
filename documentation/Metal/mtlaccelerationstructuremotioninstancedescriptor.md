# MTLAccelerationStructureMotionInstanceDescriptor

**Framework**: Metal  
**Kind**: struct

A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier and motion data for the instance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLAccelerationStructureMotionInstanceDescriptor
```

## Topics

### Creating an Instance Descriptor
- [init()](mtlaccelerationstructuremotioninstancedescriptor/init.md)
  Creates a default acceleration structure instance.
- [init(options: MTLAccelerationStructureInstanceOptions, mask: UInt32, intersectionFunctionTableOffset: UInt32, accelerationStructureIndex: UInt32, userID: UInt32, motionTransformsStartIndex: UInt32, motionTransformsCount: UInt32, motionStartBorderMode: MTLMotionBorderMode, motionEndBorderMode: MTLMotionBorderMode, motionStartTime: Float, motionEndTime: Float)](mtlaccelerationstructuremotioninstancedescriptor/init(options:mask:intersectionfunctiontableoffset:accelerationstructureindex:userid:motiontransformsstartindex:motiontransformscount:motionstartbordermode:motionendbordermode:motionstarttime:motionendtime:).md)
  Creates a new acceleration structure instance.
### Specifying the Instance
- [var accelerationStructureIndex: UInt32](mtlaccelerationstructuremotioninstancedescriptor/accelerationstructureindex.md)
  The index of the acceleration structure to use for this instance.
### Specifying Motion Data
- [var motionStartTime: Float](mtlaccelerationstructuremotioninstancedescriptor/motionstarttime.md)
  The start time for the range of motion described by the keyframe data.
- [var motionEndTime: Float](mtlaccelerationstructuremotioninstancedescriptor/motionendtime.md)
  The end time for the range of motion described by the keyframe data.
- [var motionStartBorderMode: MTLMotionBorderMode](mtlaccelerationstructuremotioninstancedescriptor/motionstartbordermode.md)
  The mode to use when handling timestamps before the start time.
- [var motionEndBorderMode: MTLMotionBorderMode](mtlaccelerationstructuremotioninstancedescriptor/motionendbordermode.md)
  The mode to use when handling timestamps after the end time.
- [var motionTransformsStartIndex: UInt32](mtlaccelerationstructuremotioninstancedescriptor/motiontransformsstartindex.md)
  The index for the instance’s first keyframe motion data.
- [var motionTransformsCount: UInt32](mtlaccelerationstructuremotioninstancedescriptor/motiontransformscount.md)
  The number of keyframes for this instance.
### Customizing Intersection and Hit Tests for the Instance
- [var intersectionFunctionTableOffset: UInt32](mtlaccelerationstructuremotioninstancedescriptor/intersectionfunctiontableoffset.md)
  An offset used to determine which function in the intersection function table Metal should call when testing a ray against this instance.
- [var options: MTLAccelerationStructureInstanceOptions](mtlaccelerationstructuremotioninstancedescriptor/options.md)
  The options for this instance.
- [var mask: UInt32](mtlaccelerationstructuremotioninstancedescriptor/mask.md)
  A mask used for this instance when testing a ray against the geometry.
### Specifying the User Identifier
- [var userID: UInt32](mtlaccelerationstructuremotioninstancedescriptor/userid.md)
  The user identifier for the instance.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MTLAccelerationStructureInstanceDescriptor](mtlaccelerationstructureinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure.
- [struct MTLAccelerationStructureUserIDInstanceDescriptor](mtlaccelerationstructureuseridinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier for the instance.
- [struct MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions.md)
  Options for adjusting the behavior of an instanced acceleration structure.
- [class MTLIndirectInstanceAccelerationStructureDescriptor](mtlindirectinstanceaccelerationstructuredescriptor.md)
  A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.
- [struct MTLIndirectAccelerationStructureInstanceDescriptor](mtlindirectaccelerationstructureinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure that the GPU can populate.
- [struct MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md)
  A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor)*