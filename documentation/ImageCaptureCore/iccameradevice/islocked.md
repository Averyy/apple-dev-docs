# isLocked

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isLocked) BOOL locked;
```

## See Also

### Deleting Files
- [struct ICDeleteResult](../icdeleteresult.md)
  The result of a deletion request.
- [struct ICDeleteError](../icdeleteerror.md)
  An error resulting from a deletion request.
- [func requestDeleteFiles([ICCameraItem])](./requestdeletefiles%28_%29.md)
  Deletes files from the camera.
- [func requestDeleteFiles([ICCameraItem], deleteFailed: ([ICDeleteError : ICCameraItem]) -> Void, completion: ([ICDeleteResult : [ICCameraItem]], (any Error)?) -> Void) -> Progress?](./requestdeletefiles%28_,deletefailed,completion%29.md)
  Deletes files from the camera, with the ability to catch failures and execute a completion block.
- [func cancelDelete()](./canceldelete%28%29.md)
  Cancels the current delete operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/islocked)*