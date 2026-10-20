# synchronizationClock

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A clock to use for output synchronization.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 13.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var synchronizationClock: CMClock? { get }
```

```objc
@property (nonatomic, readonly, nullable) CMClockRef synchronizationClock;
```

#### Discussion

The synchronization clock provides the timebase for sample buffers that the stream outputs. Use it to synchronize with the clocks of other media sources, such as the [`synchronizationClock`](../../AVFoundation/avcapturesession/synchronizationclock.md) of [`AVCaptureSession`](../../AVFoundation/avcapturesession.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/synchronizationclock)*