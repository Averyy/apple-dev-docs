# isEjectable

**Framework**: ImageCaptureCore  
**Kind**: property

A Boolean value indicating whether the device can be ‘soft’ removed or disconnected.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var isEjectable: Bool { get }
```

#### Discussion

Soft ejecting an SD card is equivalent to unmounting it in Finder without physically removing it from the host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/isejectable)*