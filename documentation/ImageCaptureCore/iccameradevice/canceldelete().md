# cancelDelete()

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Cancels the current delete operation.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func cancelDelete()
```

```objc
- (void) cancelDelete;
```

## See Also

### Deleting Files
- [var isLocked: Bool](./islocked.md)
  A Boolean value indicating whether the device is locked, preventing deletion of any asset.
- [struct ICDeleteResult](../icdeleteresult.md)
  The result of a deletion request.
- [struct ICDeleteError](../icdeleteerror.md)
  An error resulting from a deletion request.
- [func requestDeleteFiles([ICCameraItem])](./requestdeletefiles%28_%29.md)
  Deletes files from the camera.
- [func requestDeleteFiles([ICCameraItem], deleteFailed: ([ICDeleteError : ICCameraItem]) -> Void, completion: ([ICDeleteResult : [ICCameraItem]], (any Error)?) -> Void) -> Progress?](./requestdeletefiles%28_,deletefailed,completion%29.md)
  Deletes files from the camera, with the ability to catch failures and execute a completion block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/canceldelete())*