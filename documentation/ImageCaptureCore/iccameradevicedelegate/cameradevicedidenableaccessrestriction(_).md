# cameraDeviceDidEnableAccessRestriction(_:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Required**: Yes

Tells the client when an Apple device has been locked, and media is unavailable until the restriction has been removed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func cameraDeviceDidEnableAccessRestriction(_ device: ICDevice)
```

## See Also

- [func cameraDeviceDidRemoveAccessRestriction(ICDevice)](iccameradevicedelegate/cameradevicedidremoveaccessrestriction(_:).md)
  Tells the client when an Apple device has been unlocked, paired to the host, and media is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevicedidenableaccessrestriction(_:))*