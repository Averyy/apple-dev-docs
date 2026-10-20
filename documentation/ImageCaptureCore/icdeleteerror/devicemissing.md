# deviceMissing

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Type Property

The deletion failed because the device could not be found.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
static let deviceMissing: ICDeleteError
```

```c
extern ICDeleteError const ICDeleteErrorDeviceMissing;
```

## See Also

### Reading a Deletion Error
- [static let canceled: ICDeleteError](./canceled.md)
  The deletion was canceled.
- [static let fileMissing: ICDeleteError](./filemissing.md)
  The deletion failed because the file could not be found.
- [static let readOnly: ICDeleteError](./readonly.md)
  The deletion failed because the file had read-only permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdeleteerror/devicemissing)*