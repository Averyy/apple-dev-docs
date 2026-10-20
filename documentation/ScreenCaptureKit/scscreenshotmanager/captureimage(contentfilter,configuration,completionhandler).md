# captureImage(contentFilter:configuration:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Type Method

Captures a single frame from a stream as an image, using a filter.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
class func captureImage(contentFilter: SCContentFilter, configuration config: SCStreamConfiguration, completionHandler: (@Sendable (CGImage?, (any Error)?) -> Void)? = nil)
```

```swift
class func captureImage(contentFilter: SCContentFilter, configuration config: SCStreamConfiguration) async throws -> CGImage
```

```objc
+ (void) captureImageWithFilter:(SCContentFilter *) contentFilter configuration:(SCStreamConfiguration *) config completionHandler:(void (^)(CGImageRef sampleBuffer, NSError *error)) completionHandler;
```

## Parameters

- `contentFilter`: The content filter used to select the stream.
- `config`: Configuration information for how to capture the screenshot.
- `completionHandler`: Closure that processes the screenshot taken from the streaming content.

## See Also

### Individual frame capture
- [class func captureSampleBuffer(contentFilter: SCContentFilter, configuration: SCStreamConfiguration, completionHandler: ((CMSampleBuffer?, (any Error)?) -> Void)?)](./capturesamplebuffer%28contentfilter,configuration,completionhandler%29.md)
  Captures a single frame directly from a stream’s buffer, using a filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotmanager/captureimage(contentfilter:configuration:completionhandler:))*