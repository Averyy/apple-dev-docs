# startSession(atSourceTime:)

**Framework**: AVFoundation  
**Kind**: method

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

#### Discussion

You must call this method after you call [`startWriting()`](avassetwriter/startwriting().md), but before you append sample data to asset writer inputs.

Each writing session has a start time that, where allowed by the file format you’re writing, defines the mapping from the timeline of source samples to the timeline of the written file. In the case of the QuickTime movie file format, the first session begins at movie time `0`, so a sample you append with timestamp `T` plays at movie time (`T-startTime`). The writer adds samples with timestamps earlier than the start time to the output file, but they don’t display during playback. If the earliest sample for an input has a timestamp later than the start time, the system inserts an empty edit to preserve synchronization between tracks of the output asset.

To end a session, call [`endSession(atSourceTime:)`](avassetwriter/endsession(atsourcetime:).md)or [`finishWriting(completionHandler:)`](avassetwriter/finishwriting(completionhandler:).md)

> **Note**:  An asset writer doesn’t support multiple sample-writing sessions. It’s an error to call [`startSession(atSourceTime:)`](avassetwriter/startsession(atsourcetime:).md) a second time after calling [`endSession(atSourceTime:)`](avassetwriter/endsession(atsourcetime:).md).

## Parameters

- `startTime`: The starting asset time for the sample-writing session, in the timeline of the source samples.

## See Also

- [func start() throws](avassetwriter/start.md)
  Prepares the writer to write media data to its output file.
- [func startWriting() -> Bool](avassetwriter/startwriting.md)
  Tells the writer to start writing its output.
- [func endSession(atSourceTime: CMTime)](avassetwriter/endsession(atsourcetime:).md)
  Finishes an asset-writing session.
- [func finishWriting(completionHandler: () -> Void)](avassetwriter/finishwriting(completionhandler:).md)
  Marks all unfinished inputs as finished and completes the writing of the output file.
- [func cancelWriting()](avassetwriter/cancelwriting.md)
  Cancels the creation of the output file.
- [func finishWriting() -> Bool](avassetwriter/finishwriting.md)
  Completes the writing of the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/startsession(atsourcetime:))*