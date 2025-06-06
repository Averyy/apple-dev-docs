# isLocked

**Framework**: ImageCaptureCore  
**Kind**: property

A Boolean value indicating whether the device is locked, preventing deletion of any asset.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var isLocked: Bool { get }
```

## See Also

- [struct ICDeleteResult](icdeleteresult.md)
  The result of a deletion request.
- [struct ICDeleteError](icdeleteerror.md)
  An error resulting from a deletion request.
- [func requestDeleteFiles([ICCameraItem])](iccameradevice/requestdeletefiles(_:).md)
  Deletes files from the camera.
- [func requestDeleteFiles([ICCameraItem], deleteFailed: ([ICDeleteError : ICCameraItem]) -> Void, completion: ([ICDeleteResult : [ICCameraItem]], (any Error)?) -> Void) -> Progress?](iccameradevice/requestdeletefiles(_:deletefailed:completion:).md)
  Deletes files from the camera, with the ability to catch failures and execute a completion block.
- [func cancelDelete()](iccameradevice/canceldelete.md)
  Cancels the current delete operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/islocked)*