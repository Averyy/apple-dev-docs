# FSVolume.ItemDeactivationOptions

**Framework**: FSKit  
**Kind**: struct  
**Role**: Structure

Options to specify the item deactivation policy.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct ItemDeactivationOptions
```

```c
enum FSItemDeactivationOptions : NSUInteger;
```

## Overview

Callers may want to set a deactivation policy because `FSVolume/ItemDeactivation/deactivateItem(_:)` processing blocks the kernel. Setting a deactivation policy allows the file system to take action at a definitive point in the item’s life cycle. These options allow the file system to instruct the FSKit kernel of which circumstances require the expense of a round-trip call to the module.

> **Note**: To avoid performing deactivation calls, Objective-C developers use the value `FSItemDeactivationNever`. In Swift, use an empty option set (`[]`).

## Topics

### Declaring deactivation options
- [static var forRemovedItems: FSVolume.ItemDeactivationOptions](./itemdeactivationoptions/forremoveditems.md)
  An option to process deactivation for open-unlinked items at the moment of last close.
- [static var forPreallocatedItems: FSVolume.ItemDeactivationOptions](./itemdeactivationoptions/forpreallocateditems.md)
  An option to process deactivation for for files with preallocated space.
- [static var always: FSVolume.ItemDeactivationOptions](./itemdeactivationoptions/always.md)
  An option to always perform deactivation calls.
- [FSItemDeactivationNever](../fsitemdeactivationoptions/fsitemdeactivationnever.md)
  An option to never perform deactivation.
### Working with raw values
- [init(rawValue: UInt)](./itemdeactivationoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Setting deactivation policy
- [var itemDeactivationPolicy: FSVolume.ItemDeactivationOptions](./itemdeactivation/itemdeactivationpolicy.md)
  A property that tells FSKit to which types of items the deactivation applies, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/itemdeactivationoptions)*