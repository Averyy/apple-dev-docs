# instancedAccelerationStructures

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, retain, nullable) NSArray<id<MTLAccelerationStructure>> * instancedAccelerationStructures;
```

#### Discussion

Each instance in the instance descriptor buffer has an index into this array, specifying which acceleration structure to use for that instance.

## See Also

### Related Documentation
- [var accelerationStructureIndex: UInt32](../mtlaccelerationstructureinstancedescriptor/accelerationstructureindex.md)
  The index of the acceleration structure to use for the instance.
### Specifying the instance structures
- [var instanceDescriptorType: MTLAccelerationStructureInstanceDescriptorType](./instancedescriptortype.md)
  The format of the instance data in the descriptor buffer.
- [enum MTLAccelerationStructureInstanceDescriptorType](../mtlaccelerationstructureinstancedescriptortype.md)
  Options for specifying different kinds of instance types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures)*