# isSignalCompensationDelaySupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Whether adjusting the signal compensation delay property is currently supported.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var isSignalCompensationDelaySupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isSignalCompensationDelaySupported) BOOL signalCompensationDelaySupported;
```

## Discussion

This property returns `true` if the [`signalCompensationDelay`](./signalcompensationdelay.md) can be adjusted.

[`signalCompensationDelay`](./signalcompensationdelay.md) can be adjusted while the [`AVCaptureSession`](../avcapturesession.md) is not running.

Once the session is running, this property’s value depends on [`isAdjustingSignalCompensationDelayWhileRunningSupported`](../avcapturedevice/isadjustingsignalcompensationdelaywhilerunningsupported.md) of the [`AVCaptureDevice`](../avcapturedevice.md) backing the [`AVCaptureDeviceInput`](../avcapturedeviceinput.md) that is following this external sync device. Inspect that property in advance to determine whether [`signalCompensationDelay`](./signalcompensationdelay.md) will remain adjustable while running on a given device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/issignalcompensationdelaysupported)*