# MTLAccelerationStructureInstanceDescriptor

**Framework**: Metal  
**Kind**: struct

A description of an instance in an instanced geometry acceleration structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLAccelerationStructureInstanceDescriptor
```

## Topics

### Creating an instance descriptor
- [init()](mtlaccelerationstructureinstancedescriptor/init.md)
  Creates a default acceleration structure instance.
- [init(transformationMatrix: MTLPackedFloat4x3, options: MTLAccelerationStructureInstanceOptions, mask: UInt32, intersectionFunctionTableOffset: UInt32, accelerationStructureIndex: UInt32)](mtlaccelerationstructureinstancedescriptor/init(transformationmatrix:options:mask:intersectionfunctiontableoffset:accelerationstructureindex:).md)
  Creates a new acceleration structure instance.
### Specifying the instance
- [var accelerationStructureIndex: UInt32](mtlaccelerationstructureinstancedescriptor/accelerationstructureindex.md)
  The index of the acceleration structure to use for the instance.
### Specifying the instance transform
- [var transformationMatrix: MTLPackedFloat4x3](mtlaccelerationstructureinstancedescriptor/transformationmatrix.md)
  The transform for placing and orienting the instance in the scene.
### Customizing intersection and hit tests for the instance
- [var intersectionFunctionTableOffset: UInt32](mtlaccelerationstructureinstancedescriptor/intersectionfunctiontableoffset.md)
  An offset for determining which function in the intersection function table Metal needs to call when testing a ray against the instance.
- [var options: MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstancedescriptor/options.md)
  The options for the instance.
- [var mask: UInt32](mtlaccelerationstructureinstancedescriptor/mask.md)
  A mask to use for the instance when testing a ray against the geometry.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

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
- [struct MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md)
  A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptor)*