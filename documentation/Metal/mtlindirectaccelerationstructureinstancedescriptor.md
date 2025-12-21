# MTLIndirectAccelerationStructureInstanceDescriptor

**Framework**: Metal  
**Kind**: struct

A description of an instance in an instanced geometry acceleration structure that the GPU can populate.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLIndirectAccelerationStructureInstanceDescriptor
```

#### Overview

This memory layout corresponds to the [`MTLAccelerationStructureInstanceDescriptorType.indirect`](mtlaccelerationstructureinstancedescriptortype/indirect.md) instance type.

## Topics

### Initializers
- [init()](mtlindirectaccelerationstructureinstancedescriptor/init.md)
- [init(transformationMatrix: MTLPackedFloat4x3, options: MTLAccelerationStructureInstanceOptions, mask: UInt32, intersectionFunctionTableOffset: UInt32, userID: UInt32, accelerationStructureID: MTLResourceID)](mtlindirectaccelerationstructureinstancedescriptor/init(transformationmatrix:options:mask:intersectionfunctiontableoffset:userid:accelerationstructureid:).md)
### Instance Properties
- [var accelerationStructureID: MTLResourceID](mtlindirectaccelerationstructureinstancedescriptor/accelerationstructureid.md)
- [var intersectionFunctionTableOffset: UInt32](mtlindirectaccelerationstructureinstancedescriptor/intersectionfunctiontableoffset.md)
- [var mask: UInt32](mtlindirectaccelerationstructureinstancedescriptor/mask.md)
- [var options: MTLAccelerationStructureInstanceOptions](mtlindirectaccelerationstructureinstancedescriptor/options.md)
- [var transformationMatrix: MTLPackedFloat4x3](mtlindirectaccelerationstructureinstancedescriptor/transformationmatrix.md)
- [var userID: UInt32](mtlindirectaccelerationstructureinstancedescriptor/userid.md)

## Relationships

### Conforms To
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
- [struct MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md)
  A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectaccelerationstructureinstancedescriptor)*