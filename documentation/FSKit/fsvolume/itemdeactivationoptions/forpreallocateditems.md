# forPreallocatedItems

**Framework**: FSKit  
**Kind**: property

An option to process deactivation for for files with preallocated space.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var forPreallocatedItems: FSVolume.ItemDeactivationOptions { get }
```

#### Discussion

This option facilitates a sort of trim-on-close behavior. It is only meaningful for volumes that conform to [`FSVolume.PreallocateOperations`](fsvolume/preallocateoperations.md).

## See Also

- [static var forRemovedItems: FSVolume.ItemDeactivationOptions](fsvolume/itemdeactivationoptions/forremoveditems.md)
  An option to process deactivation for open-unlinked items at the moment of last close.
- [static var always: FSVolume.ItemDeactivationOptions](fsvolume/itemdeactivationoptions/always.md)
  An option to always perform deactivation calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/itemdeactivationoptions/forpreallocateditems)*