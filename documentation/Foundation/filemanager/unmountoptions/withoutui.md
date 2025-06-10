# withoutUI

**Framework**: Foundation  
**Kind**: property

Specifies that no UI should accompany the unmount operation.

**Availability**:
- macOS 10.11+

## Declaration

```swift
static var withoutUI: FileManager.UnmountOptions { get }
```

#### Discussion

If this option is not specified when calling [`unmountVolume(at:options:completionHandler:)`](filemanager/unmountvolume(at:options:completionhandler:).md), any needed UI will delay completion of the completion handler.

## See Also

- [init(rawValue: UInt)](filemanager/unmountoptions/init(rawvalue:).md)
  Creates an unmount option set from the given raw value.
- [static var allPartitionsAndEjectDisk: FileManager.UnmountOptions](filemanager/unmountoptions/allpartitionsandejectdisk.md)
  Specifies that all partitions on an unmountable disk should be unmounted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/unmountoptions/withoutui)*