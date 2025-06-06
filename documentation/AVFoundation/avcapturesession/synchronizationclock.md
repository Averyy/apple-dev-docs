# synchronizationClock

**Framework**: AVFoundation  
**Kind**: property

A clock to use for output synchronization.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var synchronizationClock: CMClock? { get }
```

#### Discussion

All capture output sample buffer timestamps are on the synchronization clock’s timebase. Use this clock in conjunction with the clock from an [`AVCaptureInput.Port`](avcaptureinput/port.md) object to synchronize capture output with external data sources such as Core Motion samples.

The example below shows how to reverse synchronize the output timestamps to the original timestamps in the [`captureOutput(_:didOutput:from:)`](avcapturevideodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:).md) method:

```swift
func captureOutput(_ output: AVCaptureOutput, didOutput sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection) {
    // Get the original and capture session clocks.
    guard let port = connection.inputPorts.first,
          let originalClock = port.clock,
          let sessionClock = captureSession?.synchronizationClock else { return }
        
    // Get the presentation timestamp of the current sample buffer.
    let syncedPTS = sampleBuffer.presentationTimeStamp
        
    // Convert the timestamp to the original timebase.
    let originalPTS = sessionClock.convertTime(syncedPTS, to: originalClock)
}
```

This property is key-value observable.

## See Also

- [var masterClock: CMClock?](avcapturesession/masterclock.md)
  A clock object used for output synchronization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/synchronizationclock)*