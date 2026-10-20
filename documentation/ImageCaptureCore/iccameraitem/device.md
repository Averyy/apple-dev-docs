# device

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The item’s parent device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var device: ICCameraDevice? { get }
```

```objc
@property (nonatomic, readonly, nullable) ICCameraDevice * device;
```

## See Also

### Locating an Item
- [var fileSystemPath: String?](./filesystempath.md)
  The item’s file system path on a camera using the mass storage transport type.
- [var parentFolder: ICCameraFolder?](./parentfolder.md)
  This item’s parent folder.
- [var isInTemporaryStore: Bool](./isintemporarystore.md)
  A Boolean value that indicates whether this item is in a temporary store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/device)*