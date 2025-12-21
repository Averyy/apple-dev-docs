# finishWriting(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Marks all unfinished inputs as finished and completes the writing of the output file.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func finishWriting() async
```

#### Discussion

To ensure the asset writer finishes writing all samples, call this method only after all calls to [`append(_:)`](avassetwriterinput/append(_:).md) or [`append(_:withPresentationTime:)`](avassetwriterinputpixelbufferadaptor/append(_:withpresentationtime:).md) return.

## Parameters

- `handler`: A completion handler the system invokes when it finishes writing. Determine the success or failure of the writing session by querying the asset writer’s   property value.

## See Also

- [func start() throws](avassetwriter/start.md)
  Prepares the writer to write media data to its output file.
- [func startWriting() -> Bool](avassetwriter/startwriting.md)
  Tells the writer to start writing its output.
- [func startSession(atSourceTime: CMTime)](avassetwriter/startsession(atsourcetime:).md)
  Starts an asset-writing session.
- [func endSession(atSourceTime: CMTime)](avassetwriter/endsession(atsourcetime:).md)
  Finishes an asset-writing session.
- [func cancelWriting()](avassetwriter/cancelwriting.md)
  Cancels the creation of the output file.
- [func finishWriting() -> Bool](avassetwriter/finishwriting.md)
  Completes the writing of the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/finishwriting(completionhandler:))*