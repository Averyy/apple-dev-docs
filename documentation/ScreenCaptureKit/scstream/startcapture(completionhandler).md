# startCapture(completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method

Starts the stream with a callback to indicate whether it successfully starts.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func startCapture(completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func startCapture() async throws
```

```objc
- (void) startCaptureWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: A completion handler that provides an error if the stream fails to start.

## See Also

### Starting and stopping a stream
- [func stopCapture(completionHandler: (((any Error)?) -> Void)?)](./stopcapture%28completionhandler%29.md)
  Stops the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/startcapture(completionhandler:))*