# MTLAccelerationStructureInstanceDescriptorType.userID

**Framework**: Metal  
**Kind**: case  
**Role**: Case

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

```c
MTLAccelerationStructureInstanceDescriptorTypeUserID
```

#### Discussion

This instance type corresponds to the [`MTLAccelerationStructureUserIDInstanceDescriptor`](../mtlaccelerationstructureuseridinstancedescriptor.md) structure memory layout.

## See Also

### Specifying the instance descriptor type
- [MTLAccelerationStructureInstanceDescriptorType.default](./default.md)
  An option specifying that the instance uses the default characteristics.
- [MTLAccelerationStructureInstanceDescriptorType.motion](./motion.md)
  An option specifying that the instance contains motion data.
- [MTLAccelerationStructureInstanceDescriptorType.indirect](./indirect.md)
  An option that enables an instance descriptor memory layout the GPU can populate.
- [MTLAccelerationStructureInstanceDescriptorType.indirectMotion](./indirectmotion.md)
  An option specifying that the instance contains motion data, and enables using an instance descriptor memory layout that the GPU can populate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptortype/userid)*