# stopCapture(completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method

Stops the stream.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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