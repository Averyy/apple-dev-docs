# always

**Framework**: FSKit  
**Kind**: property

An option to always perform deactivation calls.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var always: FSVolume.ItemDeactivationOptions { get }
```

#### Discussion

Use this option if the file system needs `deactivateItem` calls in circumstances beyond those covered by [`forRemovedItems`](fsvolume/itemdeactivationoptions/forremoveditems.md) and [`forPreallocatedItems`](fsvolume/itemdeactivationoptions/forpreallocateditems.md).

## See Also

- [static var forRemovedItems: FSVolume.ItemDeactivationOptions](fsvolume/itemdeactivationoptions/forremoveditems.md)
  An option to process deactivation for open-unlinked items at the moment of last close.
- [static var forPreallocatedItems: FSVolume.ItemDeactivationOptions](fsvolume/itemdeactivationoptions/forpreallocateditems.md)
  An option to process deactivation for for files with preallocated space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/itemdeactivationoptions/always)*