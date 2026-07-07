# smartFramingMonitor

**Framework**: AVFoundation  
**Kind**: property

A monitor owned by the device that recommends an optimal framing based on the content in the scene.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var smartFramingMonitor: AVCaptureSmartFramingMonitor? { get }
```

#### Discussion

An ultra wide camera device that supports dynamic aspect ratio configuration may also support “smart framing monitoring”. If this property returns non `nil`, you may use it to listen for framing recommendations by configuring its [`enabledFramings`](avcapturesmartframingmonitor/enabledframings.md) and calling [`startMonitoring()`](avcapturesmartframingmonitor/startmonitoring().md). The smart framing monitor only makes recommendations when the current [`activeFormat`](avcapturedevice/activeformat.md) supports smart framing (see [`isSmartFramingSupported`](avcapturedevice/format/issmartframingsupported.md)).

## See Also

- [class AVCaptureSmartFramingMonitor](avcapturesmartframingmonitor.md)
  An object associated with a capture device that monitors the scene and suggests an optimal framing.
- [class AVCaptureFraming](avcaptureframing.md)
  A framing, consisting of an aspect ratio and a zoom factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/smartframingmonitor)*