# ICDeleteError

**Framework**: ImageCaptureCore  
**Kind**: struct  
**Role**: Structure

An error resulting from a deletion request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct ICDeleteError
```

```c
typedef NSString * ICDeleteError;
```

## Topics

### Creating a Deletion Error
- [init(rawValue: String)](./icdeleteerror/init%28rawvalue%29.md)
### Reading a Deletion Error
- [static let canceled: ICDeleteError](./icdeleteerror/canceled.md)
  The deletion was canceled.
- [static let deviceMissing: ICDeleteError](./icdeleteerror/devicemissing.md)
  The deletion failed because the device could not be found.
- [static let fileMissing: ICDeleteError](./icdeleteerror/filemissing.md)
  The deletion failed because the file could not be found.
- [static let readOnly: ICDeleteError](./icdeleteerror/readonly.md)
  The deletion failed because the file had read-only permissions.

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
- [struct ICDeleteResult](./icdeleteresult.md)
  The result of a deletion request.
- [func requestDeleteFiles([ICCameraItem])](./iccameradevice/requestdeletefiles%28_%29.md)
  Deletes files from the camera.
- [func requestDeleteFiles([ICCameraItem], deleteFailed: ([ICDeleteError : ICCameraItem]) -> Void, completion: ([ICDeleteResult : [ICCameraItem]], (any Error)?) -> Void) -> Progress?](./iccameradevice/requestdeletefiles%28_,deletefailed,completion%29.md)
  Deletes files from the camera, with the ability to catch failures and execute a completion block.
- [func cancelDelete()](./iccameradevice/canceldelete%28%29.md)
  Cancels the current delete operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdeleteerror)*