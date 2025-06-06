# fileSystemPath

**Framework**: ImageCaptureCore  
**Kind**: property

The item’s file system path on a camera using the mass storage transport type.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var fileSystemPath: String? { get }
```

#### Discussion

This property is set for cameras whose [`transportType`](icdevice/transporttype.md) is [`transportTypeMassStorage`](icdevicetransport/transporttypemassstorage.md).

## See Also

- [var device: ICCameraDevice?](iccameraitem/device.md)
  The item’s parent device.
- [var parentFolder: ICCameraFolder?](iccameraitem/parentfolder.md)
  This item’s parent folder.
- [var isInTemporaryStore: Bool](iccameraitem/isintemporarystore.md)
  A Boolean value that indicates whether this item is in a temporary store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/filesystempath)*