# MTLAccelerationStructureInstanceDescriptorType.indirect

**Framework**: Metal  
**Kind**: case

An option that enables an instance descriptor memory layout the GPU can populate.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case indirect
```

#### Discussion

This instance type corresponds to the [`MTLIndirectAccelerationStructureInstanceDescriptor`](mtlindirectaccelerationstructureinstancedescriptor.md) memory layout.

## See Also

- [MTLAccelerationStructureInstanceDescriptorType.default](mtlaccelerationstructureinstancedescriptortype/default.md)
  An option specifying that the instance uses the default characteristics.
- [MTLAccelerationStructureInstanceDescriptorType.userID](mtlaccelerationstructureinstancedescriptortype/userid.md)
  An option specifying that the instance contains a user identifier.
- [MTLAccelerationStructureInstanceDescriptorType.motion](mtlaccelerationstructureinstancedescriptortype/motion.md)
  An option specifying that the instance contains motion data.
- [MTLAccelerationStructureInstanceDescriptorType.indirectMotion](mtlaccelerationstructureinstancedescriptortype/indirectmotion.md)
  An option specifying that the instance contains motion data, and enables using an instance descriptor memory layout that the GPU can populate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptortype/indirect)*