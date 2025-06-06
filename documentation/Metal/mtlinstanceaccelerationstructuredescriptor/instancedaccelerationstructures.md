# instancedAccelerationStructures

**Framework**: Metal  
**Kind**: property

The bottom-level acceleration structures that instances use in the instance acceleration structure .

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var instancedAccelerationStructures: [any MTLAccelerationStructure]? { get set }
```

#### Discussion

Each instance in the instance descriptor buffer has an index into this array, specifying which acceleration structure to use for that instance.

## See Also

- [var accelerationStructureIndex: UInt32](mtlaccelerationstructureinstancedescriptor/accelerationstructureindex.md)
  The index of the acceleration structure to use for the instance.
- [var instanceDescriptorType: MTLAccelerationStructureInstanceDescriptorType](mtlinstanceaccelerationstructuredescriptor/instancedescriptortype.md)
  The format of the instance data in the descriptor buffer.
- [enum MTLAccelerationStructureInstanceDescriptorType](mtlaccelerationstructureinstancedescriptortype.md)
  Options for specifying different kinds of instance types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures)*