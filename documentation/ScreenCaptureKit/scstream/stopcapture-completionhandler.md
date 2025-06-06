# stopCapture(completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method

Stops the stream.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
func stopCapture() async throws
```

## Parameters

- `completionHandler`: A completion handler that provides an error if the stream fails to stop.

## See Also

- [func startCapture(completionHandler: (((any Error)?) -> Void)?)](scstream/startcapture(completionhandler:).md)
  Starts the stream with a callback to indicate whether it successfully starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/stopcapture(completionhandler:))*