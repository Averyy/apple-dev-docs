# always

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

An option to always perform deactivation calls.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var always: FSVolume.ItemDeactivationOptions { get }
```

```c
FSItemDeactivationAlways
```

#### Discussion

Use this option if the file system needs `deactivateItem` calls in circumstances beyond those covered by [`forRemovedItems`](./forremoveditems.md) and [`forPreallocatedItems`](./forpreallocateditems.md).

## See Also

### Declaring deactivation options
- [static var forRemovedItems: FSVolume.ItemDeactivationOptions](./forremoveditems.md)
  An option to process deactivation for open-unlinked items at the moment of last close.
- [static var forPreallocatedItems: FSVolume.ItemDeactivationOptions](./forpreallocateditems.md)
  An option to process deactivation for for files with preallocated space.
- [FSItemDeactivationNever](../../fsitemdeactivationoptions/fsitemdeactivationnever.md)
  An option to never perform deactivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/itemdeactivationoptions/always)*