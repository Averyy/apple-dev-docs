# MTLAccelerationStructureInstanceDescriptorType.default

**Framework**: Metal  
**Kind**: case  
**Role**: Case

An option specifying that the instance uses the default characteristics.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case `default`
```

```c
MTLAccelerationStructureInstanceDescriptorTypeDefault
```

## Discussion

This instance type corresponds to the [`MTLAccelerationStructureInstanceDescriptor`](../mtlaccelerationstructureinstancedescriptor.md)  structure memory layout.

## See Also

### Specifying the instance descriptor type
- [MTLAccelerationStructureInstanceDescriptorType.userID](./userid.md)
  An option specifying that the instance contains a user identifier.
- [MTLAccelerationStructureInstanceDescriptorType.motion](./motion.md)
  An option specifying that the instance contains motion data.
- [MTLAccelerationStructureInstanceDescriptorType.indirect](./indirect.md)
  An option that enables an instance descriptor memory layout the GPU can populate.
- [MTLAccelerationStructureInstanceDescriptorType.indirectMotion](./indirectmotion.md)
  An option specifying that the instance contains motion data, and enables using an instance descriptor memory layout that the GPU can populate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptortype/default)*