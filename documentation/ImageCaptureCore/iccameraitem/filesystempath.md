# fileSystemPath

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The item’s file system path on a camera using the mass storage transport type.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var fileSystemPath: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * fileSystemPath;
```

#### Discussion

This property is set for cameras whose [`transportType`](../icdevice/transporttype.md) is [`transportTypeMassStorage`](../icdevicetransport/transporttypemassstorage.md).

## See Also

### Locating an Item
- [var device: ICCameraDevice?](./device.md)
  The item’s parent device.
- [var parentFolder: ICCameraFolder?](./parentfolder.md)
  This item’s parent folder.
- [var isInTemporaryStore: Bool](./isintemporarystore.md)
  A Boolean value that indicates whether this item is in a temporary store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/filesystempath)*