# MTLAccelerationStructureInstanceOptions

**Framework**: Metal  
**Kind**: struct

Options for adjusting the behavior of an instanced acceleration structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLAccelerationStructureInstanceOptions
```

## Topics

### Creating instance flags
- [init(rawValue: UInt32)](mtlaccelerationstructureinstanceoptions/init(rawvalue:).md)
  Creates new usage options from a raw integer value.
### Usage options
- [static var disableTriangleCulling: MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions/disabletriangleculling.md)
  An option that turns off culling for this instance if ray intersector has culling enabled.
- [static var triangleFrontFacingWindingCounterClockwise: MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions/trianglefrontfacingwindingcounterclockwise.md)
  Specifies that the instance specifies front facing triangles in counter-clockwise order.
- [static var opaque: MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions/opaque.md)
  Specifies that intersectors should treat the instance as opaque.
- [static var nonOpaque: MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions/nonopaque.md)
  Specifies that intersectors should treat the instance as non-opaque.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct MTLAccelerationStructureInstanceDescriptor](mtlaccelerationstructureinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure.
- [struct MTLAccelerationStructureUserIDInstanceDescriptor](mtlaccelerationstructureuseridinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier for the instance.
- [struct MTLAccelerationStructureMotionInstanceDescriptor](mtlaccelerationstructuremotioninstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier and motion data for the instance.
- [class MTL4IndirectInstanceAccelerationStructureDescriptor](mtl4indirectinstanceaccelerationstructuredescriptor.md)
  Descriptor for an “indirect” instance acceleration structure that allows providing the instance count and motion transform count indirectly, through buffer references.
- [class MTLIndirectInstanceAccelerationStructureDescriptor](mtlindirectinstanceaccelerationstructuredescriptor.md)
  A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.
- [struct MTLIndirectAccelerationStructureInstanceDescriptor](mtlindirectaccelerationstructureinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure that the GPU can populate.
- [struct MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md)
  A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstanceoptions)*