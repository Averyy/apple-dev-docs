# FileManager.UnmountOptions

**Framework**: Foundation  
**Kind**: struct

Options that specify the behavior of an unmount operation.

**Availability**:
- macOS 10.11+

## Declaration

```swift
struct UnmountOptions
```

## Topics

### Unmount Behavior
- [init(rawValue: UInt)](filemanager/unmountoptions/init(rawvalue:).md)
  Creates an unmount option set from the given raw value.
- [static var allPartitionsAndEjectDisk: FileManager.UnmountOptions](filemanager/unmountoptions/allpartitionsandejectdisk.md)
  Specifies that all partitions on an unmountable disk should be unmounted.
- [static var withoutUI: FileManager.UnmountOptions](filemanager/unmountoptions/withoutui.md)
  Specifies that no UI should accompany the unmount operation.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func unmountVolume(at: URL, options: FileManager.UnmountOptions, completionHandler: ((any Error)?) -> Void)](filemanager/unmountvolume(at:options:completionhandler:).md)
  Starts the process of unmounting the specified volume.
- [let NSFileManagerUnmountDissentingProcessIdentifierErrorKey: String](nsfilemanagerunmountdissentingprocessidentifiererrorkey.md)
  The process identifier of the process that prevented a volume from unmounting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/unmountoptions)*