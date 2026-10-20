# cancelWriting()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) cancelWriting;
```

#### Discussion

If the asset writer is in [`AVAssetWriter.Status.failed`](./status-swift.enum/failed.md) or [`AVAssetWriter.Status.completed`](./status-swift.enum/completed.md) state, calling this method has no effect. Otherwise, invoking it blocks the calling thread until the asset writer finishes canceling the writing session.

If the asset writer created an output file during the writing process, calling this method deletes the file.

## See Also

### Managing writing sessions
- [func start() throws](./start%28%29.md)
  Prepares the writer to write media data to its output file.
- [func startWriting() -> Bool](./startwriting%28%29.md)
  Tells the writer to start writing its output.
- [func startSession(atSourceTime: CMTime)](./startsession%28atsourcetime%29.md)
  Starts an asset-writing session.
- [func endSession(atSourceTime: CMTime)](./endsession%28atsourcetime%29.md)
  Finishes an asset-writing session.
- [func finishWriting(completionHandler: () -> Void)](./finishwriting%28completionhandler%29.md)
  Marks all unfinished inputs as finished and completes the writing of the output file.
- [func finishWriting() -> Bool](./finishwriting%28%29.md)
  Completes the writing of the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/cancelwriting())*