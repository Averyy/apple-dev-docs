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

### Creating an instance descriptor
- [init()](mtlaccelerationstructuremotioninstancedescriptor/init.md)
  Creates an acceleration-structure motion instance with default property values.
- [init(options: MTLAccelerationStructureInstanceOptions, mask: UInt32, intersectionFunctionTableOffset: UInt32, accelerationStructureIndex: UInt32, userID: UInt32, motionTransformsStartIndex: UInt32, motionTransformsCount: UInt32, motionStartBorderMode: MTLMotionBorderMode, motionEndBorderMode: MTLMotionBorderMode, motionStartTime: Float, motionEndTime: Float)](mtlaccelerationstructuremotioninstancedescriptor/init(options:mask:intersectionfunctiontableoffset:accelerationstructureindex:userid:motiontransformsstartindex:motiontransformscount:motionstartbordermode:motionendbordermode:motionstarttime:motionendtime:).md)
  Creates an acceleration-structure motion instance with the property values you provide.
### Specifying the instance
- [var accelerationStructureIndex: UInt32](mtlaccelerationstructuremotioninstancedescriptor/accelerationstructureindex.md)
  The index of an acceleration structure which applies to the next acceleration-structure motion instance you create with the descriptor.
### Specifying motion data
- [var motionStartTime: Float](mtlaccelerationstructuremotioninstancedescriptor/motionstarttime.md)
  A starting time for the range of motion that the key-frame data represents.
- [var motionEndTime: Float](mtlaccelerationstructuremotioninstancedescriptor/motionendtime.md)
  An ending time for the range of motion that the key-frame data represents.
- [var motionStartBorderMode: MTLMotionBorderMode](mtlaccelerationstructuremotioninstancedescriptor/motionstartbordermode.md)
  A behavior that configures how a motion instance handles timestamps before a starting time.
- [var motionEndBorderMode: MTLMotionBorderMode](mtlaccelerationstructuremotioninstancedescriptor/motionendbordermode.md)
  A behavior that configures how a motion instance handles timestamps after an ending time.
- [var motionTransformsStartIndex: UInt32](mtlaccelerationstructuremotioninstancedescriptor/motiontransformsstartindex.md)
  The index of motion data that represents the first key-frame motion data, which applies to the next acceleration-structure motion instance you create with the descriptor.
- [var motionTransformsCount: UInt32](mtlaccelerationstructuremotioninstancedescriptor/motiontransformscount.md)
  The number of motion data key-frames, which applies to the next acceleration-structure motion instance you create with the descriptor.
### Customizing intersection and hit tests for the instance
- [var intersectionFunctionTableOffset: UInt32](mtlaccelerationstructuremotioninstancedescriptor/intersectionfunctiontableoffset.md)
  An offset into the intersection-function table for ray tracing, which applies to the next acceleration-structure motion instance you create with the descriptor.
- [var options: MTLAccelerationStructureInstanceOptions](mtlaccelerationstructuremotioninstancedescriptor/options.md)
  An option set which applies to the next acceleration structure motion-instance you create with the descriptor.
- [var mask: UInt32](mtlaccelerationstructuremotioninstancedescriptor/mask.md)
  A mask for testing ray-tracing rays with a scene’s geometry, which applies to the next acceleration-structure motion instance you create with the descriptor.
### Specifying the user identifier
- [var userID: UInt32](mtlaccelerationstructuremotioninstancedescriptor/userid.md)
  An unique identifier, which applies to the next acceleration-structure motion instance you create with the descriptor.

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
- [class MTL4IndirectInstanceAccelerationStructureDescriptor](mtl4indirectinstanceaccelerationstructuredescriptor.md)
  Descriptor for an “indirect” instance acceleration structure that allows providing the instance count and motion transform count indirectly, through buffer references.
- [class MTLIndirectInstanceAccelerationStructureDescriptor](mtlindirectinstanceaccelerationstructuredescriptor.md)
  A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.
- [struct MTLIndirectAccelerationStructureInstanceDescriptor](mtlindirectaccelerationstructureinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure that the GPU can populate.
- [struct MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md)
  A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor)*