# FSVolume.ItemDeactivationOptions

**Framework**: Fskit  
**Kind**: struct

Options to specify the item deactivation policy.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct ItemDeactivationOptions
```

#### Overview

Callers may want to set a deactivation policy because [`deactivateItem(_:replyHandler:)`](fsvolume/itemdeactivation/deactivateitem(_:replyhandler:).md) processing blocks the kernel. Setting a deactivation policy allows the file system to take action at a definitive point in the item’s life cycle. These options allow the file system to instruct the FSKit kernel of which circumstances require the expense of a round-trip call to the module.

> **Note**: To avoid performing deactivation calls, Objective-C developers use the value `FSItemDeactivationNever`. In Swift, use an empty option set (`[]`).

## Topics

### Declaring deactivation options
- [static var forRemovedItems: FSVolume.ItemDeactivationOptions](fsvolume/itemdeactivationoptions/forremoveditems.md)
  An option to process deactivation for open-unlinked items at the moment of last close.
- [static var forPreallocatedItems: FSVolume.ItemDeactivationOptions](fsvolume/itemdeactivationoptions/forpreallocateditems.md)
  An option to process deactivation for for files with preallocated space.
- [static var always: FSVolume.ItemDeactivationOptions](fsvolume/itemdeactivationoptions/always.md)
  An option to always perform deactivation calls.
### Working with raw values
- [init(rawValue: UInt)](fsvolume/itemdeactivationoptions/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](fsvolume/itemdeactivationoptions/equatable-implementations.md)
- [OptionSet Implementations](fsvolume/itemdeactivationoptions/optionset-implementations.md)
- [SetAlgebra Implementations](fsvolume/itemdeactivationoptions/setalgebra-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var itemDeactivationPolicy: FSVolume.ItemDeactivationOptions](fsvolume/itemdeactivation/itemdeactivationpolicy.md)
  A property that tells FSKit to which types of items the deactivation applies, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/FSKit/fsvolume/itemdeactivationoptions)*