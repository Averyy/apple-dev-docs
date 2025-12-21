# instanceDescriptorType

**Framework**: Metal  
**Kind**: property

The type of instance descriptor that the instance descriptor buffer references.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var instanceDescriptorType: MTLAccelerationStructureInstanceDescriptorType { get set }
```

#### Discussion

This value determines the layout Metal expects for the structs the instance descriptor buffer contains:

- [`MTLAccelerationStructureInstanceDescriptorType.indirect`](mtlaccelerationstructureinstancedescriptortype/indirect.md): Use the [`MTLIndirectAccelerationStructureInstanceDescriptor`](mtlindirectaccelerationstructureinstancedescriptor.md) struct layout.
- [`MTLAccelerationStructureInstanceDescriptorType.indirectMotion`](mtlaccelerationstructureinstancedescriptortype/indirectmotion.md): Use the [`MTLIndirectAccelerationStructureMotionInstanceDescriptor`](mtlindirectaccelerationstructuremotioninstancedescriptor.md) struct layout.

The default value is [`MTLAccelerationStructureInstanceDescriptorType.indirect`](mtlaccelerationstructureinstancedescriptortype/indirect.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4instanceaccelerationstructuredescriptor/instancedescriptortype)*