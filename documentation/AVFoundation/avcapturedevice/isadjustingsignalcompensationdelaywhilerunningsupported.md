# isAdjustingSignalCompensationDelayWhileRunningSupported

**Framework**: AVFoundation  
**Kind**: property

Whether adjusting the signal compensation delay property of an external sync device is supported while the session is running.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var isAdjustingSignalCompensationDelayWhileRunningSupported: Bool { get }
```

#### Discussion

This property returns `true` if the `signalCompensationDelay` of an [`AVExternalSyncDevice`](avexternalsyncdevice.md) being followed by this device’s [`AVCaptureDeviceInput`](avcapturedeviceinput.md) can be adjusted while the [`AVCaptureSession`](avcapturesession.md) is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isadjustingsignalcompensationdelaywhilerunningsupported)*