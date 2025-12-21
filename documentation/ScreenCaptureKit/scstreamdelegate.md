# SCStreamDelegate

**Framework**: ScreenCaptureKit  
**Kind**: protocol

A delegate protocol your app implements to respond to stream events.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
protocol SCStreamDelegate : NSObjectProtocol
```

## Topics

### Responding to Presenter Overlay
- [func outputVideoEffectDidStart(for: SCStream)](scstreamdelegate/outputvideoeffectdidstart(for:).md)
  Tells the delegate that Presenter Overlay started.
- [func outputVideoEffectDidStop(for: SCStream)](scstreamdelegate/outputvideoeffectdidstop(for:).md)
  Tells the delegate that Presenter Overlay stopped.
### Responding to stream stoppage
- [func stream(SCStream, didStopWithError: any Error)](scstreamdelegate/stream(_:didstopwitherror:).md)
  Tells the delegate that the stream stopped with an error.
### Instance Methods
- [func streamDidBecomeActive(SCStream)](scstreamdelegate/streamdidbecomeactive(_:).md)
- [func streamDidBecomeInactive(SCStream)](scstreamdelegate/streamdidbecomeinactive(_:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SCStream](scstream.md)
  An instance that represents a stream of shareable content.
- [class SCStreamConfiguration](scstreamconfiguration.md)
  An instance that provides the output configuration for a stream.
- [class SCContentFilter](sccontentfilter.md)
  An instance that filters the content a stream captures.
- [class SCScreenshotManager](scscreenshotmanager.md)
  An instance for the capture of single frames from a stream.
- [class SCScreenshotConfiguration](scscreenshotconfiguration.md)
  An object that contains screenshot properties such as output width, height, and image quality specifications.
- [class SCScreenshotOutput](scscreenshotoutput.md)
  An object that contains all images requested by the client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamdelegate)*