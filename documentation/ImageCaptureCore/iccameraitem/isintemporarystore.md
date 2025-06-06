# isInTemporaryStore

**Framework**: ImageCaptureCore  
**Kind**: property

A Boolean value that indicates whether this item is in a temporary store.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var isInTemporaryStore: Bool { get }
```

#### Discussion

A device may use a temporary store when it captures images while tethered to a computer.

## See Also

- [var device: ICCameraDevice?](iccameraitem/device.md)
  The item’s parent device.
- [var fileSystemPath: String?](iccameraitem/filesystempath.md)
  The item’s file system path on a camera using the mass storage transport type.
- [var parentFolder: ICCameraFolder?](iccameraitem/parentfolder.md)
  This item’s parent folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/isintemporarystore)*