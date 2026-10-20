# FSVolume.CommonOperations

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Methods common to `FSVolumeHandler` and `FSVolumeOperations`

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol CommonOperations
```

```objc
@protocol FSVolumeCommonOperations
```

## Topics

### Instance Properties
- [var enableOpenUnlinkEmulation: Bool](./commonoperations/enableopenunlinkemulation.md)
  A property that allows the file system to use open-unlink emulation.
- [var requestedMountOptions: FSVolume.MountOptions](./commonoperations/requestedmountoptions.md)
  A property that allows the file system to request for specific mount options from FSKit.
- [var supportedVolumeCapabilities: FSVolume.SupportedCapabilities](./commonoperations/supportedvolumecapabilities.md)
  A property that provides the supported capabilities of the volume.
- [var volumeStatistics: FSStatFSResult](./commonoperations/volumestatistics.md)
  A property that provides up-to-date statistics of the volume.
### Instance Methods
- [func mount(options: FSTaskOptions, replyHandler: ((any Error)?) -> Void)](./commonoperations/mount%28options,replyhandler%29.md)
  Mounts this volume, using the specified options.
- [func reclaimItem(FSItem, replyHandler: ((any Error)?) -> Void)](./commonoperations/reclaimitem%28_,replyhandler%29.md)
  Reclaims an item, releasing any resources allocated for the item.
- [func synchronize(flags: FSSyncFlags, replyHandler: ((any Error)?) -> Void)](./commonoperations/synchronize%28flags,replyhandler%29.md)
  Synchronizes the volume with its underlying resource.
- [func unmount(replyHandler: () -> Void)](./commonoperations/unmount%28replyhandler%29.md)
  Unmounts this volume.

## Relationships

### Inherited By
- [FSVolume.Handler](./handler.md)
- [FSVolume.Operations](./operations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/commonoperations)*