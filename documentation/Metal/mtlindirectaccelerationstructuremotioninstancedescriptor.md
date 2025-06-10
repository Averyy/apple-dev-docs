# MTLIndirectAccelerationStructureMotionInstanceDescriptor

**Framework**: Metal  
**Kind**: struct

A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLIndirectAccelerationStructureMotionInstanceDescriptor
```

## Topics

### Specifying the Instance
- [var accelerationStructureID: MTLResourceID](mtlindirectaccelerationstructuremotioninstancedescriptor/accelerationstructureid.md)
  The acceleration resource handle to use for this instance.
### Specifying Motion Data
- [var motionStartTime: Float](mtlindirectaccelerationstructuremotioninstancedescriptor/motionstarttime.md)
  The start time of the motion instance.
- [var motionStartBorderMode: MTLMotionBorderMode](mtlindirectaccelerationstructuremotioninstancedescriptor/motionstartbordermode.md)
  The motion border mode describing what happens if Metal samples the acceleration structure before the motion start time.
- [var motionEndTime: Float](mtlindirectaccelerationstructuremotioninstancedescriptor/motionendtime.md)
  The end time of the motion instance.
- [var motionEndBorderMode: MTLMotionBorderMode](mtlindirectaccelerationstructuremotioninstancedescriptor/motionendbordermode.md)
  The motion border mode describing what happens if Metal samples the acceleration structure after the motion end time.
- [var motionTransformsCount: UInt32](mtlindirectaccelerationstructuremotioninstancedescriptor/motiontransformscount.md)
  The number of motion transforms belonging to the motion instance.
- [var motionTransformsStartIndex: UInt32](mtlindirectaccelerationstructuremotioninstancedescriptor/motiontransformsstartindex.md)
  The index of the first set of transforms describing one keyframe of the animation.
### Specifying the User Identifier
- [var userID: UInt32](mtlindirectaccelerationstructuremotioninstancedescriptor/userid.md)
  A user-assigned ID to help identify the instance.
### Initializers
- [init()](mtlindirectaccelerationstructuremotioninstancedescriptor/init.md)
  Creates a default indirect acceleration structure instance.
- [init(options: MTLAccelerationStructureInstanceOptions, mask: UInt32, intersectionFunctionTableOffset: UInt32, userID: UInt32, accelerationStructureID: MTLResourceID, motionTransformsStartIndex: UInt32, motionTransformsCount: UInt32, motionStartBorderMode: MTLMotionBorderMode, motionEndBorderMode: MTLMotionBorderMode, motionStartTime: Float, motionEndTime: Float)](mtlindirectaccelerationstructuremotioninstancedescriptor/init(options:mask:intersectionfunctiontableoffset:userid:accelerationstructureid:motiontransformsstartindex:motiontransformscount:motionstartbordermode:motionendbordermode:motionstarttime:motionendtime:).md)
  Creates an indirect acceleration structure instance.
### Instance Properties
- [var intersectionFunctionTableOffset: UInt32](mtlindirectaccelerationstructuremotioninstancedescriptor/intersectionfunctiontableoffset.md)
  An offset for determining which function in the intersection function table Metal calls when testing a ray against the instance.
- [var mask: UInt32](mtlindirectaccelerationstructuremotioninstancedescriptor/mask.md)
  An instance mask to ignore geometry during ray tracing.
- [var options: MTLAccelerationStructureInstanceOptions](mtlindirectaccelerationstructuremotioninstancedescriptor/options.md)
  The options for this instance.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MTLAccelerationStructureInstanceDescriptor](mtlaccelerationstructureinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure.
- [struct MTLAccelerationStructureUserIDInstanceDescriptor](mtlaccelerationstructureuseridinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier for the instance.
- [struct MTLAccelerationStructureMotionInstanceDescriptor](mtlaccelerationstructuremotioninstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier and motion data for the instance.
- [struct MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions.md)
  Options for adjusting the behavior of an instanced acceleration structure.
- [class MTL4IndirectInstanceAccelerationStructureDescriptor](mtl4indirectinstanceaccelerationstructuredescriptor.md)
  Descriptor for an “indirect” instance acceleration structure that allows providing the instance count and motion transform count indirectly, through buffer references.
- [class MTLIndirectInstanceAccelerationStructureDescriptor](mtlindirectinstanceaccelerationstructuredescriptor.md)
  A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.
- [struct MTLIndirectAccelerationStructureInstanceDescriptor](mtlindirectaccelerationstructureinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure that the GPU can populate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor)*