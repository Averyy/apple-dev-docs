# ICDeleteResult

**Framework**: ImageCaptureCore  
**Kind**: struct

The result of a deletion request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct ICDeleteResult
```

## Topics

### Creating a Deletion Result
- [init(rawValue: String)](icdeleteresult/init(rawvalue:).md)
### Reading a Deletion Result
- [static let canceled: ICDeleteResult](icdeleteresult/canceled.md)
  The deletion was canceled.
- [static let failed: ICDeleteResult](icdeleteresult/failed.md)
  The deletion failed.
- [static let successful: ICDeleteResult](icdeleteresult/successful.md)
  The deletion succeeded.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var isLocked: Bool](iccameradevice/islocked.md)
  A Boolean value indicating whether the device is locked, preventing deletion of any asset.
- [struct ICDeleteError](icdeleteerror.md)
  An error resulting from a deletion request.
- [func requestDeleteFiles([ICCameraItem])](iccameradevice/requestdeletefiles(_:).md)
  Deletes files from the camera.
- [func requestDeleteFiles([ICCameraItem], deleteFailed: ([ICDeleteError : ICCameraItem]) -> Void, completion: ([ICDeleteResult : [ICCameraItem]], (any Error)?) -> Void) -> Progress?](iccameradevice/requestdeletefiles(_:deletefailed:completion:).md)
  Deletes files from the camera, with the ability to catch failures and execute a completion block.
- [func cancelDelete()](iccameradevice/canceldelete.md)
  Cancels the current delete operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdeleteresult)*