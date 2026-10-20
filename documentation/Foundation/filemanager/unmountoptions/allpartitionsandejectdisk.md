# allPartitionsAndEjectDisk

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Specifies that all partitions on an unmountable disk should be unmounted.

**Availability**:
- macOS 10.11+

## Declaration

```swift
static var allPartitionsAndEjectDisk: FileManager.UnmountOptions { get }
```

```c
NSFileManagerUnmountAllPartitionsAndEjectDisk
```

#### Discussion

If the volume is on a partitioned disk, this option unmounts all volumes on that disk. Then, then the disk is ejected (if it is ejectable).

## See Also

### Unmount Behavior
- [init(rawValue: UInt)](./init%28rawvalue%29.md)
  Creates an unmount option set from the given raw value.
- [static var withoutUI: FileManager.UnmountOptions](./withoutui.md)
  Specifies that no UI should accompany the unmount operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/unmountoptions/allpartitionsandejectdisk)*