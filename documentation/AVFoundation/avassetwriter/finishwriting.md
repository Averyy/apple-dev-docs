# finishWriting()

**Framework**: AVFoundation  
**Kind**: method

Completes the writing of the output file.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
func finishWriting() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if writing can be finished, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/finishwriting())*