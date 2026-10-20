# endSession(atSourceTime:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Finishes an asset-writing session.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func endSession(atSourceTime endTime: CMTime)
```

```objc
- (void) endSessionAtSourceTime:(CMTime) endTime;
```

#### Discussion

Call this method to complete a session that you started with [`startSession(atSourceTime:)`](./startsession%28atsourcetime%29.md).

The end time defines the moment on the timeline of source samples at which the session ends. In the case of the QuickTime movie file format, each sample-writing session’s start and end time pair corresponds to a period of movie time into which a writer inserts samples. The writer adds samples with timestamps that are later than the session end time to the written file but they aren’t presented during playback. For example, if the first session has duration `D1 = endTime - startTime`, the writer inserts it into the written file at time `0` through `D1`; the second session would insert into the written file at time `D1` through `D1 + D2`, and so on. It’s legal to have a session with no samples; this causes the creation of an empty edit of the prescribed duration.

If you don’t explicitly call this method, the system invokes it automatically when you call [`finishWriting(completionHandler:)`](./finishwriting%28completionhandler%29.md). In that case, the session’s effective end time is the timestamp of the last sample you append.

> **Note**:  An asset writer doesn’t support multiple sample-writing sessions. It’s an error to call [`startSession(atSourceTime:)`](./startsession%28atsourcetime%29.md) a second time after calling [`endSession(atSourceTime:)`](./endsession%28atsourcetime%29.md).

## Parameters

- `endTime`: The ending asset time for the session, in the timeline of the source samples.

## See Also

### Managing writing sessions
- [func start() throws](./start%28%29.md)
  Prepares the writer to write media data to its output file.
- [func startWriting() -> Bool](./startwriting%28%29.md)
  Tells the writer to start writing its output.
- [func startSession(atSourceTime: CMTime)](./startsession%28atsourcetime%29.md)
  Starts an asset-writing session.
- [func finishWriting(completionHandler: () -> Void)](./finishwriting%28completionhandler%29.md)
  Marks all unfinished inputs as finished and completes the writing of the output file.
- [func cancelWriting()](./cancelwriting%28%29.md)
  Cancels the creation of the output file.
- [func finishWriting() -> Bool](./finishwriting%28%29.md)
  Completes the writing of the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/endsession(atsourcetime:))*