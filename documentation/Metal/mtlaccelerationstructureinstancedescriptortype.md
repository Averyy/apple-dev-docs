# MTLAccelerationStructureInstanceDescriptorType

**Framework**: Metal  
**Kind**: enum

Options for specifying different kinds of instance types.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLAccelerationStructureInstanceDescriptorType
```

## Topics

### Specifying the Instance Descriptor Type
- [MTLAccelerationStructureInstanceDescriptorType.default](mtlaccelerationstructureinstancedescriptortype/default.md)
  An option specifying that the instance uses the default characteristics.
- [MTLAccelerationStructureInstanceDescriptorType.userID](mtlaccelerationstructureinstancedescriptortype/userid.md)
  An option specifying that the instance contains a user identifier.
- [MTLAccelerationStructureInstanceDescriptorType.motion](mtlaccelerationstructureinstancedescriptortype/motion.md)
  An option specifying that the instance contains motion data.
- [MTLAccelerationStructureInstanceDescriptorType.indirect](mtlaccelerationstructureinstancedescriptortype/indirect.md)
  An option that enables using an instance descriptor memory layout that the GPU can populate.
- [MTLAccelerationStructureInstanceDescriptorType.indirectMotion](mtlaccelerationstructureinstancedescriptortype/indirectmotion.md)
  An option specifying that the instance contains motion data, and enables using an instance descriptor memory layout that the GPU can populate.
### Initializers
- [init?(rawValue: UInt)](mtlaccelerationstructureinstancedescriptortype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var instanceDescriptorType: MTLAccelerationStructureInstanceDescriptorType](mtlinstanceaccelerationstructuredescriptor/instancedescriptortype.md)
  The format of the instance data in the descriptor buffer.
- [var instancedAccelerationStructures: [any MTLAccelerationStructure]?](mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures.md)
  The bottom-level acceleration structures that instances use in the instance acceleration structure .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptortype)*