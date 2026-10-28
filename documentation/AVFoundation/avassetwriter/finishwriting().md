# finishWriting()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Completes the writing of the output file.

**Availability**:
- tvOS 9.0+ - Deprecated in 9.0

> **Deprecated**: Use [`finishWriting(completionHandler:)`](./finishwriting%28completionhandler%29.md) instead.

## Declaration

```swift
func finishWriting() -> Bool
```

```objc
- (BOOL) finishWriting;
```

## Return Value

[`true`](../../Swift/true.md) if writing can be finished, otherwise [`false`](../../Swift/false.md).

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
- [func cancelWriting()](./cancelwriting%28%29.md)
  Cancels the creation of the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/finishwriting())*