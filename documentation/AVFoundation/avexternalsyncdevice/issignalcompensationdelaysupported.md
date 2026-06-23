# isSignalCompensationDelaySupported

**Framework**: AVFoundation  
**Kind**: property

Whether adjusting the signal compensation delay property is currently supported.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var isSignalCompensationDelaySupported: Bool { get }
```

#### Discussion

This property returns `true` if the [`signalCompensationDelay`](avexternalsyncdevice/signalcompensationdelay.md) can be adjusted.

[`signalCompensationDelay`](avexternalsyncdevice/signalcompensationdelay.md) can be adjusted while the [`AVCaptureSession`](avcapturesession.md) is not running.

Once the session is running, this property’s value depends on [`isAdjustingSignalCompensationDelayWhileRunningSupported`](avcapturedevice/isadjustingsignalcompensationdelaywhilerunningsupported.md) of the [`AVCaptureDevice`](avcapturedevice.md) backing the [`AVCaptureDeviceInput`](avcapturedeviceinput.md) that is following this external sync device. Inspect that property in advance to determine whether [`signalCompensationDelay`](avexternalsyncdevice/signalcompensationdelay.md) will remain adjustable while running on a given device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/issignalcompensationdelaysupported)*