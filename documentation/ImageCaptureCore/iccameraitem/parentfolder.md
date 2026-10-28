# parentFolder

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

This item’s parent folder.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var parentFolder: ICCameraFolder? { get }
```

```objc
@property (nonatomic, readonly, nullable) ICCameraFolder * parentFolder;
```

## Discussion

The value of this property on the root folder is nil.

## See Also

### Locating an Item
- [var device: ICCameraDevice?](./device.md)
  The item’s parent device.
- [var fileSystemPath: String?](./filesystempath.md)
  The item’s file system path on a camera using the mass storage transport type.
- [var isInTemporaryStore: Bool](./isintemporarystore.md)
  A Boolean value that indicates whether this item is in a temporary store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/parentfolder)*