# SCContentFilter

**Framework**: ScreenCaptureKit  
**Kind**: class

An instance that filters the content a stream captures.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
class SCContentFilter
```

#### Overview

Use a content filter to limit an [`SCStream`](scstream.md) object’s output to only that matching your filter criteria. Retrieve the displays, apps, and windows that your app can capture from an instance of [`SCShareableContent`](scshareablecontent.md).

## Topics

### Creating a filter
- [init(desktopIndependentWindow: SCWindow)](sccontentfilter/init(desktopindependentwindow:).md)
  Creates a filter that captures only the specified window.
- [init(display: SCDisplay, including: [SCWindow])](sccontentfilter/init(display:including:).md)
  Creates a filter that captures only specific windows from a display.
- [init(display: SCDisplay, excludingWindows: [SCWindow])](sccontentfilter/init(display:excludingwindows:).md)
  Creates a filter that captures the contents of a display, excluding the specified windows.
- [init(display: SCDisplay, including: [SCRunningApplication], exceptingWindows: [SCWindow])](sccontentfilter/init(display:including:exceptingwindows:).md)
  Creates a filter that captures a display, including only windows of the specified apps.
- [init(display: SCDisplay, excludingApplications: [SCRunningApplication], exceptingWindows: [SCWindow])](sccontentfilter/init(display:excludingapplications:exceptingwindows:).md)
  Creates a filter that captures a display, excluding windows of the specified apps.
### Filter properties
- [var contentRect: CGRect](sccontentfilter/contentrect.md)
  The size and location of the content to filter, in screen points.
- [var pointPixelScale: Float](sccontentfilter/pointpixelscale.md)
  The scaling factor used to translate screen points into pixels.
- [var streamType: SCStreamType](sccontentfilter/streamtype.md)
  The type of the streaming content.
- [enum SCStreamType](scstreamtype.md)
  The display type of the presented stream.
- [var style: SCShareableContentStyle](sccontentfilter/style.md)
  The display style of the sharable content.
### Instance Properties
- [var includeMenuBar: Bool](sccontentfilter/includemenubar.md)
- [var includedApplications: [SCRunningApplication]](sccontentfilter/includedapplications.md)
- [var includedDisplays: [SCDisplay]](sccontentfilter/includeddisplays.md)
- [var includedWindows: [SCWindow]](sccontentfilter/includedwindows.md)

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
- [protocol SCStreamDelegate](scstreamdelegate.md)
  A delegate protocol your app implements to respond to stream events.
- [class SCScreenshotManager](scscreenshotmanager.md)
  An instance for the capture of single frames from a stream.
- [class SCScreenshotConfiguration](scscreenshotconfiguration.md)
- [class SCScreenshotOutput](scscreenshotoutput.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentfilter)*