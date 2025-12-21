# start()

**Framework**: AVFoundation  
**Kind**: method

Prepares the writer to write media data to its output file.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func start() throws
```

#### Discussion

> **Note**: An error if reading fails to start.

## See Also

- [func startWriting() -> Bool](avassetwriter/startwriting.md)
  Tells the writer to start writing its output.
- [func startSession(atSourceTime: CMTime)](avassetwriter/startsession(atsourcetime:).md)
  Starts an asset-writing session.
- [func endSession(atSourceTime: CMTime)](avassetwriter/endsession(atsourcetime:).md)
  Finishes an asset-writing session.
- [func finishWriting(completionHandler: () -> Void)](avassetwriter/finishwriting(completionhandler:).md)
  Marks all unfinished inputs as finished and completes the writing of the output file.
- [func cancelWriting()](avassetwriter/cancelwriting.md)
  Cancels the creation of the output file.
- [func finishWriting() -> Bool](avassetwriter/finishwriting.md)
  Completes the writing of the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/start())*