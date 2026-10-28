# forPreallocatedItems

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

An option to process deactivation for for files with preallocated space.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var forPreallocatedItems: FSVolume.ItemDeactivationOptions { get }
```

```c
FSItemDeactivationForPreallocatedItems
```

## Discussion

This option facilitates a sort of trim-on-close behavior. It is only meaningful for volumes that conform to [`FSVolume.PreallocateHandler`](../preallocatehandler.md).

## See Also

### Declaring deactivation options
- [static var forRemovedItems: FSVolume.ItemDeactivationOptions](./forremoveditems.md)
  An option to process deactivation for open-unlinked items at the moment of last close.
- [static var always: FSVolume.ItemDeactivationOptions](./always.md)
  An option to always perform deactivation calls.
- [FSItemDeactivationNever](../../fsitemdeactivationoptions/fsitemdeactivationnever.md)
  An option to never perform deactivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/itemdeactivationoptions/forpreallocateditems)*