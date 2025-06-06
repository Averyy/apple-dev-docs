# markAsFinished()

**Framework**: AVFoundation  
**Kind**: method

Marks the input as finished to indicate that you’re done appending samples to it.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func markAsFinished()
```

#### Discussion

Apps that monitor an input’s [`isReadyForMoreMediaData`](avassetwriterinput/isreadyformoremediadata.md) value must call this method when they finish appending to it. This is necessary to prevent other inputs from stalling because they’re waiting on the input’s media data to complete the ideal interleaving pattern.

After calling this method from the serial queue passed to [`requestMediaDataWhenReady(on:using:)`](avassetwriterinput/requestmediadatawhenready(on:using:).md), the input issues no more invocations of the callback it passes to that method.

## See Also

- [var expectsMediaDataInRealTime: Bool](avassetwriterinput/expectsmediadatainrealtime.md)
  A Boolean value that indicates whether the input tailors its processing for real-time sources.
- [var isReadyForMoreMediaData: Bool](avassetwriterinput/isreadyformoremediadata.md)
  A Boolean value that indicates whether the input is ready to accept media data.
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](avassetwriterinput/requestmediadatawhenready(on:using:).md)
  Tells the input to request media data, at its convenience, to write to the output file.
- [func append(CMSampleBuffer) -> Bool](avassetwriterinput/append(_:).md)
  Appends a sample buffer to an input to write to the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/markasfinished())*