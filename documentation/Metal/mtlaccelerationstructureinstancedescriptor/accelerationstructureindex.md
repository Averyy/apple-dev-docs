# accelerationStructureIndex

**Framework**: Metal  
**Kind**: property

The index of the acceleration structure to use for the instance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var accelerationStructureIndex: UInt32
```

#### Discussion

This index refers to a bottom-level instance in the [`instancedAccelerationStructures`](mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures.md) of the [`MTLInstanceAccelerationStructureDescriptor`](mtlinstanceaccelerationstructuredescriptor.md) that you use to create the new instance acceleration structure.

## See Also

- [var instancedAccelerationStructures: [any MTLAccelerationStructure]?](mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures.md)
  The bottom-level acceleration structures that instances use in the instance acceleration structure .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptor/accelerationstructureindex)*