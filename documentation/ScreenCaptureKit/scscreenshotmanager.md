# SCScreenshotManager

**Framework**: ScreenCaptureKit  
**Kind**: class

An instance for the capture of single frames from a stream.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
class SCScreenshotManager
```

## Topics

### Individual frame capture
- [class func captureImage(contentFilter: SCContentFilter, configuration: SCStreamConfiguration, completionHandler: ((CGImage?, (any Error)?) -> Void)?)](scscreenshotmanager/captureimage(contentfilter:configuration:completionhandler:).md)
  Captures a single frame from a stream as an image, using a filter.
- [class func captureSampleBuffer(contentFilter: SCContentFilter, configuration: SCStreamConfiguration, completionHandler: ((CMSampleBuffer?, (any Error)?) -> Void)?)](scscreenshotmanager/capturesamplebuffer(contentfilter:configuration:completionhandler:).md)
  Captures a single frame directly from a stream’s buffer, using a filter.
### Type Methods
- [class func captureImage(in: CGRect, completionHandler: ((CGImage?, (any Error)?) -> Void)?)](scscreenshotmanager/captureimage(in:completionhandler:).md)
- [class func captureScreenshot(contentFilter: SCContentFilter, configuration: SCScreenshotConfiguration, completionHandler: ((SCScreenshotOutput?, (any Error)?) -> Void)?)](scscreenshotmanager/capturescreenshot(contentfilter:configuration:completionhandler:).md)
- [class func captureScreenshot(rect: CGRect, configuration: SCScreenshotConfiguration, completionHandler: ((SCScreenshotOutput?, (any Error)?) -> Void)?)](scscreenshotmanager/capturescreenshot(rect:configuration:completionhandler:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SCStream](scstream.md)
  An instance that represents a stream of shareable content.
- [class SCStreamConfiguration](scstreamconfiguration.md)
  An instance that provides the output configuration for a stream.
- [class SCContentFilter](sccontentfilter.md)
  An instance that filters the content a stream captures.
- [protocol SCStreamDelegate](scstreamdelegate.md)
  A delegate protocol your app implements to respond to stream events.
- [class SCScreenshotConfiguration](scscreenshotconfiguration.md)
  An object that contains screenshot properties such as output width, height, and image quality specifications.
- [class SCScreenshotOutput](scscreenshotoutput.md)
  An object that contains all images requested by the client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotmanager)*