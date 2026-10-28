# SCContentFilter

**Framework**: ScreenCaptureKit  
**Kind**: class  
**Role**: Class

An instance that filters the content a stream captures.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class SCContentFilter
```

```objc
@interface SCContentFilter : NSObject
```

## Overview

Use a content filter to limit an [`SCStream`](./scstream.md) object’s output to only that matching your filter criteria. Retrieve the displays, apps, and windows that your app can capture from an instance of [`SCShareableContent`](./scshareablecontent.md).

## Topics

### Creating a filter
- [init(desktopIndependentWindow: SCWindow)](./sccontentfilter/init%28desktopindependentwindow%29.md)
  Creates a filter that captures only the specified window.
- [init(display: SCDisplay, including: [SCWindow])](./sccontentfilter/init%28display,including%29.md)
  Creates a filter that captures only specific windows from a display.
- [init(display: SCDisplay, excludingWindows: [SCWindow])](./sccontentfilter/init%28display,excludingwindows%29.md)
  Creates a filter that captures the contents of a display, excluding the specified windows.
- [init(display: SCDisplay, including: [SCRunningApplication], exceptingWindows: [SCWindow])](./sccontentfilter/init%28display,including,exceptingwindows%29.md)
  Creates a filter that captures a display, including only windows of the specified apps.
- [init(display: SCDisplay, excludingApplications: [SCRunningApplication], exceptingWindows: [SCWindow])](./sccontentfilter/init%28display,excludingapplications,exceptingwindows%29.md)
  Creates a filter that captures a display, excluding windows of the specified apps.
### Filter properties
- [var contentRect: CGRect](./sccontentfilter/contentrect.md)
  The size and location of the content to filter, in screen points.
- [var pointPixelScale: Float](./sccontentfilter/pointpixelscale.md)
  The scaling factor used to translate screen points into pixels.
- [var streamType: SCStreamType](./sccontentfilter/streamtype.md)
  The type of the streaming content.
- [enum SCStreamType](./scstreamtype.md)
  The display type of the presented stream.
- [var style: SCShareableContentStyle](./sccontentfilter/style.md)
  The display style of the sharable content.
### Initializers
- [init(display: SCDisplay, includingApplications: [SCRunningApplication], exceptingWindows: [SCWindow])](./sccontentfilter/init%28display,includingapplications,exceptingwindows%29.md)
- [init(display: SCDisplay, includingWindows: [SCWindow])](./sccontentfilter/init%28display,includingwindows%29.md)
### Instance Properties
- [var includeMenuBar: Bool](./sccontentfilter/includemenubar.md)
- [var includedApplications: [SCRunningApplication]](./sccontentfilter/includedapplications.md)
- [var includedDisplays: [SCDisplay]](./sccontentfilter/includeddisplays.md)
- [var includedWindows: [SCWindow]](./sccontentfilter/includedwindows.md)
- [var isCameraEnabled: Bool](./sccontentfilter/iscameraenabled.md)
- [var isMicrophoneEnabled: Bool](./sccontentfilter/ismicrophoneenabled.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Content capture
- [class SCStream](./scstream.md)
  An instance that represents a stream of shareable content.
- [class SCStreamConfiguration](./scstreamconfiguration.md)
  An instance that provides the output configuration for a stream.
- [protocol SCStreamDelegate](./scstreamdelegate.md)
  A delegate protocol your app implements to respond to stream events.
- [class SCScreenshotManager](./scscreenshotmanager.md)
  An instance for the capture of single frames from a stream.
- [class SCScreenshotConfiguration](./scscreenshotconfiguration.md)
  An object that contains screenshot properties such as output width, height, and image quality specifications.
- [class SCScreenshotOutput](./scscreenshotoutput.md)
  An object that contains all images requested by the client.
- [class SCVideoEffectOutput](./scvideoeffectoutput.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentfilter)*