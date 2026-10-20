# readOnly

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Type Property

The deletion failed because the file had read-only permissions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
static let readOnly: ICDeleteError
```

```c
extern ICDeleteError const ICDeleteErrorReadOnly;
```

## See Also

### Reading a Deletion Error
- [static let canceled: ICDeleteError](./canceled.md)
  The deletion was canceled.
- [static let deviceMissing: ICDeleteError](./devicemissing.md)
  The deletion failed because the device could not be found.
- [static let fileMissing: ICDeleteError](./filemissing.md)
  The deletion failed because the file could not be found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdeleteerror/readonly)*