# masterClock

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A clock object used for output synchronization.

**Availability**:
- iOS 7.0+ - Deprecated in 15.4
- iPadOS 7.0+ - Deprecated in 15.4
- Mac Catalyst 14.0+ - Deprecated in 15.4
- macOS 10.9+ - Deprecated in 12.3

> **Deprecated**: Use [`synchronizationClock`](./synchronizationclock.md) instead.

## Declaration

```swift
var masterClock: CMClock? { get }
```

```objc
@property (nonatomic, readonly, nullable) CMClockRef masterClock;
```

## Discussion

The returned [`CMClock`](../../CoreMedia/cmclock.md) object is read-only and provides a timebase for all sample buffers in capture output. Use this clock in conjunction with the clock from an [`AVCaptureInput.Port`](../avcaptureinput/port.md) object to synchronize capture output with external data sources such as motion samples.

For example, to synchronize output timestamps to the original timestamps provided by an input device, you can do the following in your [`fileOutput(_:didOutputSampleBuffer:from:)`](../avcapturefileoutputdelegate/fileoutput%28_,didoutputsamplebuffer,from%29.md) method:

```swift
guard let masterClock = captureSession.masterClock,
    let originalClock = connection.inputPorts.first?.clock else { return }

let synchedPTS = sampleBuffer.presentationTimeStamp
let originalPTS = masterClock.convertTime(synchedPTS, to: originalClock)
```

This property is key-value observable.

## See Also

### Synchronizing output
- [var synchronizationClock: CMClock?](./synchronizationclock.md)
  A clock to use for output synchronization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/masterclock)*