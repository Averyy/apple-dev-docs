# synchronizationClock

**Framework**: ScreenCaptureKit  
**Kind**: property

A clock to use for output synchronization.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.2+
- macOS 13.0+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var synchronizationClock: CMClock? { get }
```

#### Discussion

The synchronization clock provides the timebase for sample buffers that the stream outputs. Use it to synchronize with the clocks of other media sources, such as the [`synchronizationClock`](https://developer.apple.com/documentation/avfoundation/avcapturesession/synchronizationclock) of [`AVCaptureSession`](https://developer.apple.com/documentation/avfoundation/avcapturesession).


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/synchronizationclock)*