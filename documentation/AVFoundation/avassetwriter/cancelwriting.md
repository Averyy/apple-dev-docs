# cancelWriting()

**Framework**: AVFoundation  
**Kind**: method

Cancels the creation of the output file.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func cancelWriting()
```

#### Discussion

If the asset writer is in [`AVAssetWriter.Status.failed`](avassetwriter/status-swift.enum/failed.md) or [`AVAssetWriter.Status.completed`](avassetwriter/status-swift.enum/completed.md) state, calling this method has no effect. Otherwise, invoking it blocks the calling thread until the asset writer finishes canceling the writing session.

If the asset writer created an output file during the writing process, calling this method deletes the file.

## See Also

- [func start() throws](avassetwriter/start.md)
  Prepares the writer to write media data to its output file.
- [func startWriting() -> Bool](avassetwriter/startwriting.md)
  Tells the writer to start writing its output.
- [func startSession(atSourceTime: CMTime)](avassetwriter/startsession(atsourcetime:).md)
  Starts an asset-writing session.
- [func endSession(atSourceTime: CMTime)](avassetwriter/endsession(atsourcetime:).md)
  Finishes an asset-writing session.
- [func finishWriting(completionHandler: () -> Void)](avassetwriter/finishwriting(completionhandler:).md)
  Marks all unfinished inputs as finished and completes the writing of the output file.
- [func finishWriting() -> Bool](avassetwriter/finishwriting.md)
  Completes the writing of the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/cancelwriting())*