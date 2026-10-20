# mountPoint

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The file system mount point for a camera using the mass storage transport type.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var mountPoint: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * mountPoint;
```

#### Discussion

This property is set for cameras whose [`transportType`](../icdevice/transporttype.md) is [`transportTypeMassStorage`](../icdevicetransport/transporttypemassstorage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/mountpoint)*