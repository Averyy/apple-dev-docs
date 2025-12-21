# MTL4IndirectInstanceAccelerationStructureDescriptor

**Framework**: Metal  
**Kind**: class

Descriptor for an “indirect” instance acceleration structure that allows providing the instance count and motion transform count indirectly, through buffer references.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class MTL4IndirectInstanceAccelerationStructureDescriptor
```

#### Overview

An instance acceleration structure references other acceleration structures, and provides the ability to “instantiate” them multiple times, each one with potentially a different transformation matrix.

You specify the properties of the instances in the acceleration structure this descriptor builds by providing a buffer of `structs` via its [`instanceDescriptorBuffer`](mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptorbuffer.md) property.

Compared to [`MTL4InstanceAccelerationStructureDescriptor`](mtl4instanceaccelerationstructuredescriptor.md), this descriptor allows you to provide the number of instances it references indirectly through a buffer reference, as well as the number of motion transforms.

This enables you to determine these counts indirectly in the GPU timeline via a compute pipeline. Metal needs only to know the maximum possible number of instances and motion transforms to support, which you specify via the [`maxInstanceCount`](mtl4indirectinstanceaccelerationstructuredescriptor/maxinstancecount.md) and [`maxMotionTransformCount`](mtl4indirectinstanceaccelerationstructuredescriptor/maxmotiontransformcount.md) properties.

Use a [`MTLResidencySet`](mtlresidencyset.md) to mark residency of all buffers and acceleration structures this descriptor references when you build this acceleration structure.

## Topics

### Instance Properties
- [var instanceCountBuffer: MTL4BufferRange](mtl4indirectinstanceaccelerationstructuredescriptor/instancecountbuffer.md)
  Provides a reference to a buffer containing the number of instances in the instance descriptor buffer, formatted as a 32-bit unsigned integer.
- [var instanceDescriptorBuffer: MTL4BufferRange](mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptorbuffer.md)
  Assigns a reference to a buffer containing instance descriptors for acceleration structures to reference.
- [var instanceDescriptorStride: Int](mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptorstride.md)
  Sets the stride, in bytes, between instance descriptors in the instance descriptor buffer.
- [var instanceDescriptorType: MTLAccelerationStructureInstanceDescriptorType](mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptortype.md)
  Controls the type of instance descriptor that the instance descriptor buffer references.
- [var instanceTransformationMatrixLayout: MTLMatrixLayout](mtl4indirectinstanceaccelerationstructuredescriptor/instancetransformationmatrixlayout.md)
  Specifies the layout for the transformation matrices in the instance descriptor buffer and the motion transformation matrix buffer.
- [var maxInstanceCount: Int](mtl4indirectinstanceaccelerationstructuredescriptor/maxinstancecount.md)
  Controls the maximum number of instance descriptors the instance descriptor buffer can reference.
- [var maxMotionTransformCount: Int](mtl4indirectinstanceaccelerationstructuredescriptor/maxmotiontransformcount.md)
  Controls the maximum number of motion transforms in the motion transform buffer.
- [var motionTransformBuffer: MTL4BufferRange](mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformbuffer.md)
  A buffer containing transformation information for instance motion keyframes, formatted according to the motion transform type.
- [var motionTransformCountBuffer: MTL4BufferRange](mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformcountbuffer.md)
  Associates a buffer reference containing the number of motion transforms in the motion transform buffer, formatted as a 32-bit unsigned integer.
- [var motionTransformStride: Int](mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformstride.md)
  Sets the stride for motion transform.
- [var motionTransformType: MTLTransformType](mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformtype.md)
  Sets the type of motion transforms, either as a matrix or individual components.

## Relationships

### Inherits From
- [MTL4AccelerationStructureDescriptor](mtl4accelerationstructuredescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct MTLAccelerationStructureInstanceDescriptor](mtlaccelerationstructureinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure.
- [struct MTLAccelerationStructureUserIDInstanceDescriptor](mtlaccelerationstructureuseridinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier for the instance.
- [struct MTLAccelerationStructureMotionInstanceDescriptor](mtlaccelerationstructuremotioninstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier and motion data for the instance.
- [struct MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions.md)
  Options for adjusting the behavior of an instanced acceleration structure.
- [class MTLIndirectInstanceAccelerationStructureDescriptor](mtlindirectinstanceaccelerationstructuredescriptor.md)
  A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.
- [struct MTLIndirectAccelerationStructureInstanceDescriptor](mtlindirectaccelerationstructureinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure that the GPU can populate.
- [struct MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md)
  A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor)*