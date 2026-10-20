# canceled

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Type Property

The deletion was canceled.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
static let canceled: ICDeleteError
```

```c
extern ICDeleteError const ICDeleteErrorCanceled;
```

## See Also

### Reading a Deletion Error
- [static let deviceMissing: ICDeleteError](./devicemissing.md)
  The deletion failed because the device could not be found.
- [static let fileMissing: ICDeleteError](./filemissing.md)
  The deletion failed because the file could not be found.
- [static let readOnly: ICDeleteError](./readonly.md)
  The deletion failed because the file had read-only permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdeleteerror/canceled)*