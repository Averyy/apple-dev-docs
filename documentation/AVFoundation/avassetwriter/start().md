# start()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Prepares the writer to write media data to its output file.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func start() throws
```

#### Discussion

> **Throws**: An error if reading fails to start.

## See Also

### Managing writing sessions
- [func startWriting() -> Bool](./startwriting%28%29.md)
  Tells the writer to start writing its output.
- [func startSession(atSourceTime: CMTime)](./startsession%28atsourcetime%29.md)
  Starts an asset-writing session.
- [func endSession(atSourceTime: CMTime)](./endsession%28atsourcetime%29.md)
  Finishes an asset-writing session.
- [func finishWriting(completionHandler: () -> Void)](./finishwriting%28completionhandler%29.md)
  Marks all unfinished inputs as finished and completes the writing of the output file.
- [func cancelWriting()](./cancelwriting%28%29.md)
  Cancels the creation of the output file.
- [func finishWriting() -> Bool](./finishwriting%28%29.md)
  Completes the writing of the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/start())*