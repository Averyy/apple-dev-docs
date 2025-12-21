# accelerationStructureIndex

**Framework**: Metal  
**Kind**: property

The index of an acceleration structure which applies to the next acceleration-structure motion instance you create with the descriptor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var accelerationStructureIndex: UInt32
```

#### Discussion

This index refers to a bottom-level instance specified in the [`instancedAccelerationStructures`](mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures.md) of the [`MTLInstanceAccelerationStructureDescriptor`](mtlinstanceaccelerationstructuredescriptor.md) used to create the new instance acceleration structure.

## See Also

- [var instancedAccelerationStructures: [any MTLAccelerationStructure]?](mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures.md)
  The bottom-level acceleration structures that instances use in the instance acceleration structure .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/accelerationstructureindex)*