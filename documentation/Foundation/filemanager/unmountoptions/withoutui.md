# withoutUI

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Specifies that no UI should accompany the unmount operation.

**Availability**:
- macOS 10.11+

## Declaration

```swift
static var withoutUI: FileManager.UnmountOptions { get }
```

```c
NSFileManagerUnmountWithoutUI
```

## Discussion

If this option is not specified when calling [`unmountVolume(at:options:completionHandler:)`](../unmountvolume%28at,options,completionhandler%29.md), any needed UI will delay completion of the completion handler.

## See Also

### Unmount Behavior
- [init(rawValue: UInt)](./init%28rawvalue%29.md)
  Creates an unmount option set from the given raw value.
- [static var allPartitionsAndEjectDisk: FileManager.UnmountOptions](./allpartitionsandejectdisk.md)
  Specifies that all partitions on an unmountable disk should be unmounted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/unmountoptions/withoutui)*