# MTLAccelerationStructureInstanceDescriptorType.userID

**Framework**: Metal  
**Kind**: case

An option specifying that the instance contains a user identifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case userID
```

#### Discussion

This instance type corresponds to the [`MTLAccelerationStructureUserIDInstanceDescriptor`](mtlaccelerationstructureuseridinstancedescriptor.md) structure memory layout.

## See Also

- [MTLAccelerationStructureInstanceDescriptorType.default](mtlaccelerationstructureinstancedescriptortype/default.md)
  An option specifying that the instance uses the default characteristics.
- [MTLAccelerationStructureInstanceDescriptorType.motion](mtlaccelerationstructureinstancedescriptortype/motion.md)
  An option specifying that the instance contains motion data.
- [MTLAccelerationStructureInstanceDescriptorType.indirect](mtlaccelerationstructureinstancedescriptortype/indirect.md)
  An option that enables using an instance descriptor memory layout that the GPU can populate.
- [MTLAccelerationStructureInstanceDescriptorType.indirectMotion](mtlaccelerationstructureinstancedescriptortype/indirectmotion.md)
  An option specifying that the instance contains motion data, and enables using an instance descriptor memory layout that the GPU can populate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptortype/userid)*