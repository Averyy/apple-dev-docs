# captureImage(contentFilter:configuration:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method

Captures a single frame from a stream as an image, using a filter.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
class func captureImage(contentFilter: SCContentFilter, configuration config: SCStreamConfiguration) async throws -> CGImage
```

## Parameters

- `contentFilter`: The content filter used to select the stream.
- `config`: Configuration information for how to capture the screenshot.
- `completionHandler`: Closure that processes the screenshot taken from the streaming content.

## See Also

- [class func captureSampleBuffer(contentFilter: SCContentFilter, configuration: SCStreamConfiguration, completionHandler: ((CMSampleBuffer?, (any Error)?) -> Void)?)](scscreenshotmanager/capturesamplebuffer(contentfilter:configuration:completionhandler:).md)
  Captures a single frame directly from a stream’s buffer, using a filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotmanager/captureimage(contentfilter:configuration:completionhandler:))*