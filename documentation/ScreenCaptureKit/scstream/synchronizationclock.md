# synchronizationClock

**Framework**: ScreenCaptureKit  
**Kind**: property

A clock to use for output synchronization.

**Availability**:
- Mac Catalyst 16.1+
- macOS 13.0+

## Declaration

```swift
var synchronizationClock: CMClock? { get }
```

#### Discussion

The synchronization clock provides the timebase for sample buffers that the stream outputs. Use it to synchronize with the clocks of other media sources, such as the [`synchronizationClock`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/synchronizationClock) of [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession).


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/synchronizationclock)*