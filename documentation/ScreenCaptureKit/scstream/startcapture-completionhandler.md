# startCapture(completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method

Starts the stream with a callback to indicate whether it successfully starts.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
func startCapture() async throws
```

## Parameters

- `completionHandler`: A completion handler that provides an error if the stream fails to start.

## See Also

- [func stopCapture(completionHandler: (((any Error)?) -> Void)?)](scstream/stopcapture(completionhandler:).md)
  Stops the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/startcapture(completionhandler:))*