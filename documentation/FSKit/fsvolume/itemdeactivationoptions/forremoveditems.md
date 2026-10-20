# forRemovedItems

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

An option to process deactivation for open-unlinked items at the moment of last close.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var forRemovedItems: FSVolume.ItemDeactivationOptions { get }
```

```c
FSItemDeactivationForRemovedItems
```

## See Also

### Declaring deactivation options
- [static var forPreallocatedItems: FSVolume.ItemDeactivationOptions](./forpreallocateditems.md)
  An option to process deactivation for for files with preallocated space.
- [static var always: FSVolume.ItemDeactivationOptions](./always.md)
  An option to always perform deactivation calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/itemdeactivationoptions/forremoveditems)*