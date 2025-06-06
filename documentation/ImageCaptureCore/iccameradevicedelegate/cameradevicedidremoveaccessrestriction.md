# cameraDeviceDidRemoveAccessRestriction(_:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Required**: Yes

Tells the client when an Apple device has been unlocked, paired to the host, and media is available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func cameraDeviceDidRemoveAccessRestriction(_ device: ICDevice)
```

## See Also

- [func cameraDeviceDidEnableAccessRestriction(ICDevice)](iccameradevicedelegate/cameradevicedidenableaccessrestriction(_:).md)
  Tells the client when an Apple device has been locked, and media is unavailable until the restriction has been removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevicedidremoveaccessrestriction(_:))*