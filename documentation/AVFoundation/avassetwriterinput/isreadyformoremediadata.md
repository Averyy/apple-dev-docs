# isReadyForMoreMediaData

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the input is ready to accept media data.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isReadyForMoreMediaData: Bool { get }
```

#### Discussion

An asset writer with multiple inputs writes media data in an interleaved manner for efficient playback and storage. To maintain appropriate interleaving, you can only append data to an input when the value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

Apps that write media data from a non-real-time source, such as an instance of [`AVAssetReader`](avassetreader.md), wait to generate or retrieve more media data while this property value is [`false`](https://developer.apple.com/documentation/swift/false). To control of the supply of non-real-time media data, use the [`requestMediaDataWhenReady(on:using:)`](avassetwriterinput/requestmediadatawhenready(on:using:).md) method to specify a callback for the input to invoke when it’s ready to append more data.

Apps that write media data from a real-time source, such as an instance of [`AVCaptureOutput`](avcaptureoutput.md), set the input’s [`expectsMediaDataInRealTime`](avassetwriterinput/expectsmediadatainrealtime.md) property value to [`true`](https://developer.apple.com/documentation/swift/true) so that the input accurately determines its readiness for more data. When [`expectsMediaDataInRealTime`](avassetwriterinput/expectsmediadatainrealtime.md) is [`true`](https://developer.apple.com/documentation/swift/true), this property value becomes [`false`](https://developer.apple.com/documentation/swift/false) only when the input can’t process media samples at the current data rate. If this property value becomes [`false`](https://developer.apple.com/documentation/swift/false) for a real-time source, your app may need to reduce the rate at which it appends samples, or drop them altogether.

If the [`canPerformMultiplePasses`](avassetwriterinput/canperformmultiplepasses.md) value of any of an asset writer’s inputs is [`true`](https://developer.apple.com/documentation/swift/true), the value of this property may start as [`false`](https://developer.apple.com/documentation/swift/false), and remain that way for extended periods.

The value of this property often changes from [`false`](https://developer.apple.com/documentation/swift/false) to [`true`](https://developer.apple.com/documentation/swift/true) asynchronously, as the asset writer processes and writes media samples to the output. It’s possible for this property value to temporarily be [`false`](https://developer.apple.com/documentation/swift/false) for all inputs.

This property is key-value observable. The system doesn’t notify observers on a specific thread.

## See Also

- [var expectsMediaDataInRealTime: Bool](avassetwriterinput/expectsmediadatainrealtime.md)
  A Boolean value that indicates whether the input tailors its processing for real-time sources.
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](avassetwriterinput/requestmediadatawhenready(on:using:).md)
  Tells the input to request media data, at its convenience, to write to the output file.
- [func append(CMSampleBuffer) -> Bool](avassetwriterinput/append(_:).md)
  Appends a sample buffer to an input to write to the output file.
- [func markAsFinished()](avassetwriterinput/markasfinished.md)
  Marks the input as finished to indicate that you’re done appending samples to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/isreadyformoremediadata)*