# MTLIndirectInstanceAccelerationStructureDescriptor

**Framework**: Metal  
**Kind**: class

A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class MTLIndirectInstanceAccelerationStructureDescriptor
```

## Topics

### Instance Properties
- [var instanceCountBuffer: (any MTLBuffer)?](mtlindirectinstanceaccelerationstructuredescriptor/instancecountbuffer.md)
- [var instanceCountBufferOffset: Int](mtlindirectinstanceaccelerationstructuredescriptor/instancecountbufferoffset.md)
- [var instanceDescriptorBuffer: (any MTLBuffer)?](mtlindirectinstanceaccelerationstructuredescriptor/instancedescriptorbuffer.md)
- [var instanceDescriptorBufferOffset: Int](mtlindirectinstanceaccelerationstructuredescriptor/instancedescriptorbufferoffset.md)
- [var instanceDescriptorStride: Int](mtlindirectinstanceaccelerationstructuredescriptor/instancedescriptorstride.md)
- [var instanceDescriptorType: MTLAccelerationStructureInstanceDescriptorType](mtlindirectinstanceaccelerationstructuredescriptor/instancedescriptortype.md)
- [var instanceTransformationMatrixLayout: MTLMatrixLayout](mtlindirectinstanceaccelerationstructuredescriptor/instancetransformationmatrixlayout.md)
- [var maxInstanceCount: Int](mtlindirectinstanceaccelerationstructuredescriptor/maxinstancecount.md)
- [var maxMotionTransformCount: Int](mtlindirectinstanceaccelerationstructuredescriptor/maxmotiontransformcount.md)
- [var motionTransformBuffer: (any MTLBuffer)?](mtlindirectinstanceaccelerationstructuredescriptor/motiontransformbuffer.md)
- [var motionTransformBufferOffset: Int](mtlindirectinstanceaccelerationstructuredescriptor/motiontransformbufferoffset.md)
- [var motionTransformCountBuffer: (any MTLBuffer)?](mtlindirectinstanceaccelerationstructuredescriptor/motiontransformcountbuffer.md)
- [var motionTransformCountBufferOffset: Int](mtlindirectinstanceaccelerationstructuredescriptor/motiontransformcountbufferoffset.md)
- [var motionTransformStride: Int](mtlindirectinstanceaccelerationstructuredescriptor/motiontransformstride.md)
- [var motionTransformType: MTLTransformType](mtlindirectinstanceaccelerationstructuredescriptor/motiontransformtype.md)

## Relationships

### Inherits From
- [MTLAccelerationStructureDescriptor](mtlaccelerationstructuredescriptor.md)
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
- [struct MTLIndirectAccelerationStructureInstanceDescriptor](mtlindirectaccelerationstructureinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure that the GPU can populate.
- [struct MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md)
  A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectinstanceaccelerationstructuredescriptor)*