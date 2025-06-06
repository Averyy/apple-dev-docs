# mountPoint

**Framework**: ImageCaptureCore  
**Kind**: property

The file system mount point for a camera using the mass storage transport type.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var mountPoint: String? { get }
```

#### Discussion

This property is set for cameras whose [`transportType`](icdevice/transporttype.md) is [`transportTypeMassStorage`](icdevicetransport/transporttypemassstorage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/mountpoint)*