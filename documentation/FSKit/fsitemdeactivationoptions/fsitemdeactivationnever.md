# FSItemDeactivationNever

**Framework**: FSKit  
**Kind**: case  
**Role**: Enumeration Case

An option to never perform deactivation.

**Availability**:
- macOS 15.4+

## Declaration

```c
FSItemDeactivationNever
```

## Discussion

With this deactivation option, FSKit never issues `deactivateItem` calls, even though the volume conforms to [`FSVolume.ItemDeactivation`](../fsvolume/itemdeactivation.md).

## See Also

### Declaring deactivation options
- [static var forRemovedItems: FSVolume.ItemDeactivationOptions](../fsvolume/itemdeactivationoptions/forremoveditems.md)
  An option to process deactivation for open-unlinked items at the moment of last close.
- [static var forPreallocatedItems: FSVolume.ItemDeactivationOptions](../fsvolume/itemdeactivationoptions/forpreallocateditems.md)
  An option to process deactivation for for files with preallocated space.
- [static var always: FSVolume.ItemDeactivationOptions](../fsvolume/itemdeactivationoptions/always.md)
  An option to always perform deactivation calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitemdeactivationoptions/fsitemdeactivationnever)*