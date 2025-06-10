# allPartitionsAndEjectDisk

**Framework**: Foundation  
**Kind**: property

Specifies that all partitions on an unmountable disk should be unmounted.

**Availability**:
- macOS 10.11+

## Declaration

```swift
static var allPartitionsAndEjectDisk: FileManager.UnmountOptions { get }
```

#### Discussion

If the volume is on a partitioned disk, this option unmounts all volumes on that disk. Then, then the disk is ejected (if it is ejectable).

## See Also

- [init(rawValue: UInt)](filemanager/unmountoptions/init(rawvalue:).md)
  Creates an unmount option set from the given raw value.
- [static var withoutUI: FileManager.UnmountOptions](filemanager/unmountoptions/withoutui.md)
  Specifies that no UI should accompany the unmount operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/unmountoptions/allpartitionsandejectdisk)*