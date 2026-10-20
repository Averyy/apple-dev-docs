# startWriting()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the writer to start writing its output.

**Availability**:
- iOS 4.1+ - Deprecated in 27.0
- iPadOS 4.1+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use start() instead

## Declaration

```swift
func startWriting() -> Bool
```

```objc
- (BOOL) startWriting;
```

#### Return Value

[`true`](../../Swift/true.md) if writing starts successfully; otherwise [`false`](../../Swift/false.md).

#### Discussion

You must call this method after you configure the writer and add its inputs to prepare the object to write data. After you call this method, your app can start writing sessions by calling [`startSession(atSourceTime:)`](./startsession%28atsourcetime%29.md) and can write media samples using the methods that the asset writer’s inputs provide.

If writing fails to start, this method returns [`false`](../../Swift/false.md). In this case, check the values of the [`status`](./status-swift.property.md) and [`error`](./error.md) properties to determine the reason for the failure.

## See Also

### Managing writing sessions
- [func start() throws](./start%28%29.md)
  Prepares the writer to write media data to its output file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/startwriting())*