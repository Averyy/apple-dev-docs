# requestDeleteFiles(_:deleteFailed:completion:)

**Framework**: ImageCaptureCore  
**Kind**: method

Deletes files from the camera, with the ability to catch failures and execute a completion block.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func requestDeleteFiles(_ files: [ICCameraItem], deleteFailed: @escaping ([ICDeleteError : ICCameraItem]) -> Void, completion: @escaping ([ICDeleteResult : [ICCameraItem]], (any Error)?) -> Void) -> Progress?
```

## See Also

- [var isLocked: Bool](iccameradevice/islocked.md)
  A Boolean value indicating whether the device is locked, preventing deletion of any asset.
- [struct ICDeleteResult](icdeleteresult.md)
  The result of a deletion request.
- [struct ICDeleteError](icdeleteerror.md)
  An error resulting from a deletion request.
- [func requestDeleteFiles([ICCameraItem])](iccameradevice/requestdeletefiles(_:).md)
  Deletes files from the camera.
- [func cancelDelete()](iccameradevice/canceldelete.md)
  Cancels the current delete operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/requestdeletefiles(_:deletefailed:completion:))*