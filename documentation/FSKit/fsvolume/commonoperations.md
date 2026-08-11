# FSVolume.CommonOperations

**Framework**: FSKit  
**Kind**: protocol

Methods common to `FSVolumeHandler` and `FSVolumeOperations`

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol CommonOperations
```

## Topics

### Instance Properties
- [var enableOpenUnlinkEmulation: Bool](fsvolume/commonoperations/enableopenunlinkemulation.md)
  A property that allows the file system to use open-unlink emulation.
- [var requestedMountOptions: FSVolume.MountOptions](fsvolume/commonoperations/requestedmountoptions.md)
  A property that allows the file system to request for specific mount options from FSKit.
- [var supportedVolumeCapabilities: FSVolume.SupportedCapabilities](fsvolume/commonoperations/supportedvolumecapabilities.md)
  A property that provides the supported capabilities of the volume.
- [var volumeStatistics: FSStatFSResult](fsvolume/commonoperations/volumestatistics.md)
  A property that provides up-to-date statistics of the volume.
### Instance Methods
- [func mount(options: FSTaskOptions, replyHandler: ((any Error)?) -> Void)](fsvolume/commonoperations/mount(options:replyhandler:).md)
  Mounts this volume, using the specified options.
- [func reclaimItem(FSItem, replyHandler: ((any Error)?) -> Void)](fsvolume/commonoperations/reclaimitem(_:replyhandler:).md)
  Reclaims an item, releasing any resources allocated for the item.
- [func synchronize(flags: FSSyncFlags, replyHandler: ((any Error)?) -> Void)](fsvolume/commonoperations/synchronize(flags:replyhandler:).md)
  Synchronizes the volume with its underlying resource.
- [func unmount(replyHandler: () -> Void)](fsvolume/commonoperations/unmount(replyhandler:).md)
  Unmounts this volume.

## Relationships

### Inherited By
- [FSVolume.Handler](fsvolume/handler.md)
- [FSVolume.Operations](fsvolume/operations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/commonoperations)*