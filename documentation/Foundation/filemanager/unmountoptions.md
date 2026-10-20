# FileManager.UnmountOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Options that specify the behavior of an unmount operation.

**Availability**:
- macOS 10.11+

## Declaration

```swift
struct UnmountOptions
```

```c
enum NSFileManagerUnmountOptions : NSUInteger;
```

## Topics

### Unmount Behavior
- [init(rawValue: UInt)](./unmountoptions/init%28rawvalue%29.md)
  Creates an unmount option set from the given raw value.
- [static var allPartitionsAndEjectDisk: FileManager.UnmountOptions](./unmountoptions/allpartitionsandejectdisk.md)
  Specifies that all partitions on an unmountable disk should be unmounted.
- [static var withoutUI: FileManager.UnmountOptions](./unmountoptions/withoutui.md)
  Specifies that no UI should accompany the unmount operation.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Unmounting volumes
- [func unmountVolume(at: URL, options: FileManager.UnmountOptions, completionHandler: ((any Error)?) -> Void)](./unmountvolume%28at,options,completionhandler%29.md)
  Starts the process of unmounting the specified volume.
- [let NSFileManagerUnmountDissentingProcessIdentifierErrorKey: String](../nsfilemanagerunmountdissentingprocessidentifiererrorkey.md)
  The process identifier of the process that prevented a volume from unmounting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/unmountoptions)*