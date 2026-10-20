# finishWriting(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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
func finishWriting(completionHandler handler: @escaping @Sendable () -> Void)
```

```swift
func finishWriting() async
```

```objc
- (void) finishWritingWithCompletionHandler:(void (^)()) handler;
```

#### Discussion

To ensure the asset writer finishes writing all samples, call this method only after all calls to [`append(_:)`](../avassetwriterinput/append%28_%29.md) or [`append(_:withPresentationTime:)`](../avassetwriterinputpixelbufferadaptor/append%28_,withpresentationtime%29.md) return.

## Parameters

- `handler`: A completion handler the system invokes when it finishes writing. Determine the success or failure of the writing session by querying the asset writer’s [`status`](./status-swift.property.md) property value.

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
- [func cancelWriting()](./cancelwriting%28%29.md)
  Cancels the creation of the output file.
- [func finishWriting() -> Bool](./finishwriting%28%29.md)
  Completes the writing of the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/finishwriting(completionhandler:))*