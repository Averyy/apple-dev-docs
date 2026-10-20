# ICDeleteResult

**Framework**: ImageCaptureCore  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * ICDeleteResult;
```

## Topics

### Creating a Deletion Result
- [init(rawValue: String)](./icdeleteresult/init%28rawvalue%29.md)
### Reading a Deletion Result
- [static let canceled: ICDeleteResult](./icdeleteresult/canceled.md)
  The deletion was canceled.
- [static let failed: ICDeleteResult](./icdeleteresult/failed.md)
  The deletion failed.
- [static let successful: ICDeleteResult](./icdeleteresult/successful.md)
  The deletion succeeded.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deleting Files
- [var isLocked: Bool](./iccameradevice/islocked.md)
  A Boolean value indicating whether the device is locked, preventing deletion of any asset.
- [struct ICDeleteError](./icdeleteerror.md)
  An error resulting from a deletion request.
- [func requestDeleteFiles([ICCameraItem])](./iccameradevice/requestdeletefiles%28_%29.md)
  Deletes files from the camera.
- [func requestDeleteFiles([ICCameraItem], deleteFailed: ([ICDeleteError : ICCameraItem]) -> Void, completion: ([ICDeleteResult : [ICCameraItem]], (any Error)?) -> Void) -> Progress?](./iccameradevice/requestdeletefiles%28_,deletefailed,completion%29.md)
  Deletes files from the camera, with the ability to catch failures and execute a completion block.
- [func cancelDelete()](./iccameradevice/canceldelete%28%29.md)
  Cancels the current delete operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdeleteresult)*