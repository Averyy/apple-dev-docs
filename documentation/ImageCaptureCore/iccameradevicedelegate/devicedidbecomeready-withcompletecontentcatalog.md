# deviceDidBecomeReady(withCompleteContentCatalog:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Required**: Yes

Tells the client that the camera device is done enumerating its content and is ready to receive requests.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func deviceDidBecomeReady(withCompleteContentCatalog device: ICCameraDevice)
```

#### Discussion

You must open a session on the device before you can enumerate its content and make it ready to receive requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/devicedidbecomeready(withcompletecontentcatalog:))*