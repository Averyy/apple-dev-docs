# MTLResidencySetDescriptor

**Framework**: Metal  
**Kind**: class

A configuration that customizes the behavior for a residency set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class MTLResidencySetDescriptor
```

## Mentions

- [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Overview

Make an [`MTLResidencySet`](mtlresidencyset.md) by creating and configuring an [`MTLResidencySetDescriptor`](mtlresidencysetdescriptor.md) instance and pass it to the [`makeResidencySet(descriptor:)`](mtldevice/makeresidencyset(descriptor:).md) method of an [`MTLDevice`](mtldevice.md) instance.

See [`Simplifying GPU resource management with residency sets`](simplifying-gpu-resource-management-with-residency-sets.md) for more information.

## Topics

### Configuring the residency set
- [var label: String?](mtlresidencysetdescriptor/label.md)
  An optional name that can help you identify a residency set you create with the descriptor.
- [var initialCapacity: Int](mtlresidencysetdescriptor/initialcapacity.md)
  The number of allocations a new residency set can store without reallocating memory.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md)
  Organize your resources into groups and influence when they become accessible to the GPU.
- [protocol MTLResidencySet](mtlresidencyset.md)
  A collection of resource allocations that can move in and out of resident memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencysetdescriptor)*