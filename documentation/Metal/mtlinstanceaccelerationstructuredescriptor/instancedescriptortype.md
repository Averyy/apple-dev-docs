# instanceDescriptorType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The format of the instance data in the descriptor buffer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var instanceDescriptorType: MTLAccelerationStructureInstanceDescriptorType { get set }
```

```objc
@property (nonatomic) MTLAccelerationStructureInstanceDescriptorType instanceDescriptorType;
```

## See Also

### Related Documentation
- [var instanceDescriptorBuffer: (any MTLBuffer)?](./instancedescriptorbuffer.md)
  A buffer that contains descriptions of each instance in the acceleration structure.
### Specifying the instance structures
- [var instancedAccelerationStructures: [any MTLAccelerationStructure]?](./instancedaccelerationstructures.md)
  The bottom-level acceleration structures that instances use in the instance acceleration structure .
- [enum MTLAccelerationStructureInstanceDescriptorType](../mtlaccelerationstructureinstancedescriptortype.md)
  Options for specifying different kinds of instance types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptortype)*