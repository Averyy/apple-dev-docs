# MTLAccelerationStructureUserIDInstanceDescriptor

**Framework**: Metal  
**Kind**: struct

A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier for the instance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLAccelerationStructureUserIDInstanceDescriptor
```

## Topics

### Creating an Instance Descriptor
- [init()](mtlaccelerationstructureuseridinstancedescriptor/init.md)
  Creates a default acceleration structure instance.
- [init(transformationMatrix: MTLPackedFloat4x3, options: MTLAccelerationStructureInstanceOptions, mask: UInt32, intersectionFunctionTableOffset: UInt32, accelerationStructureIndex: UInt32, userID: UInt32)](mtlaccelerationstructureuseridinstancedescriptor/init(transformationmatrix:options:mask:intersectionfunctiontableoffset:accelerationstructureindex:userid:).md)
  Creates a new acceleration structure instance.
### Specifying the Instance
- [var accelerationStructureIndex: UInt32](mtlaccelerationstructureuseridinstancedescriptor/accelerationstructureindex.md)
  The index of the acceleration structure to use for the instance.
### Specifying the Instance Transform
- [var transformationMatrix: MTLPackedFloat4x3](mtlaccelerationstructureuseridinstancedescriptor/transformationmatrix.md)
  The transform for placing and orienting the instance in the scene.
### Customizing Intersection and Hit Tests for the Instance
- [var intersectionFunctionTableOffset: UInt32](mtlaccelerationstructureuseridinstancedescriptor/intersectionfunctiontableoffset.md)
  An offset for determining which function in the intersection function table Metal calls when testing a ray against the instance.
- [var options: MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureuseridinstancedescriptor/options.md)
  The options for the instance.
- [var mask: UInt32](mtlaccelerationstructureuseridinstancedescriptor/mask.md)
  A mask to use for the instance when testing a ray against the geometry.
### Specifying the User Identifier
- [var userID: UInt32](mtlaccelerationstructureuseridinstancedescriptor/userid.md)
  The user identifier for the instance.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MTLAccelerationStructureInstanceDescriptor](mtlaccelerationstructureinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureuseridinstancedescriptor)*