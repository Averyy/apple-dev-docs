# captureSampleBuffer(contentFilter:configuration:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method

Captures a single frame directly from a stream’s buffer, using a filter.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
class func captureSampleBuffer(contentFilter: SCContentFilter, configuration config: SCStreamConfiguration) async throws -> CMSampleBuffer
```

## Parameters

- `contentFilter`: The content filter used to select the stream.
- `config`: Configuration information for how to record the stream buffer.
- `completionHandler`: Closure that processes the capture taken from streaming content.

## See Also

- [class func captureImage(contentFilter: SCContentFilter, configuration: SCStreamConfiguration, completionHandler: ((CGImage?, (any Error)?) -> Void)?)](scscreenshotmanager/captureimage(contentfilter:configuration:completionhandler:).md)
  Captures a single frame from a stream as an image, using a filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotmanager/capturesamplebuffer(contentfilter:configuration:completionhandler:))*