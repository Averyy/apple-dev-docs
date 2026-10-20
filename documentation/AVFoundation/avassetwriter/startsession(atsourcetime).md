# startSession(atSourceTime:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Starts an asset-writing session.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func startSession(atSourceTime startTime: CMTime)
```

```objc
- (void) startSessionAtSourceTime:(CMTime) startTime;
```

#### Discussion

You must call this method after you call [`startWriting()`](./startwriting%28%29.md), but before you append sample data to asset writer inputs.

Each writing session has a start time that, where allowed by the file format you’re writing, defines the mapping from the timeline of source samples to the timeline of the written file. In the case of the QuickTime movie file format, the first session begins at movie time `0`, so a sample you append with timestamp `T` plays at movie time (`T-startTime`). The writer adds samples with timestamps earlier than the start time to the output file, but they don’t display during playback. If the earliest sample for an input has a timestamp later than the start time, the system inserts an empty edit to preserve synchronization between tracks of the output asset.

To end a session, call [`endSession(atSourceTime:)`](./endsession%28atsourcetime%29.md)or [`finishWriting(completionHandler:)`](./finishwriting%28completionhandler%29.md)

> **Note**:  An asset writer doesn’t support multiple sample-writing sessions. It’s an error to call [`startSession(atSourceTime:)`](./startsession%28atsourcetime%29.md) a second time after calling [`endSession(atSourceTime:)`](./endsession%28atsourcetime%29.md).

## Parameters

- `startTime`: The starting asset time for the sample-writing session, in the timeline of the source samples.

## See Also

### Managing writing sessions
- [func start() throws](./start%28%29.md)
  Prepares the writer to write media data to its output file.
- [func startWriting() -> Bool](./startwriting%28%29.md)
  Tells the writer to start writing its output.
- [func endSession(atSourceTime: CMTime)](./endsession%28atsourcetime%29.md)
  Finishes an asset-writing session.
- [func finishWriting(completionHandler: () -> Void)](./finishwriting%28completionhandler%29.md)
  Marks all unfinished inputs as finished and completes the writing of the output file.
- [func cancelWriting()](./cancelwriting%28%29.md)
  Cancels the creation of the output file.
- [func finishWriting() -> Bool](./finishwriting%28%29.md)
  Completes the writing of the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/startsession(atsourcetime:))*