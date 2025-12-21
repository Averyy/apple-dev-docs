# startWriting()

**Framework**: AVFoundation  
**Kind**: method

Tells the writer to start writing its output.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func startWriting() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if writing starts successfully; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

You must call this method after you configure the writer and add its inputs to prepare the object to write data. After you call this method, your app can start writing sessions by calling [`startSession(atSourceTime:)`](avassetwriter/startsession(atsourcetime:).md) and can write media samples using the methods that the asset writer’s inputs provide.

If writing fails to start, this method returns [`false`](https://developer.apple.com/documentation/Swift/false). In this case, check the values of the [`status`](avassetwriter/status-swift.property.md) and [`error`](avassetwriter/error.md) properties to determine the reason for the failure.

## See Also

- [func start() throws](avassetwriter/start.md)
  Prepares the writer to write media data to its output file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/startwriting())*