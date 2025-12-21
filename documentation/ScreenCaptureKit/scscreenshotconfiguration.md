# SCScreenshotConfiguration

**Framework**: ScreenCaptureKit  
**Kind**: class

An object that contains screenshot properties such as output width, height, and image quality specifications.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
class SCScreenshotConfiguration
```

#### Overview

`SCScreenshotConfiguration` provides a default image capture configuration for [`SCScreenshotManager`](scscreenshotmanager.md). Only configure its properties if you need to customize the output. Additional options for customization include dynamic range settings, image reproduction optimizations, and ignoring user interface elements.

## Topics

### Instance Properties
- [var contentType: UTTypeReference](scscreenshotconfiguration/contenttype.md)
  A uniform type identifier that specifies the screenshot’s file format; HEIC, JPEG, or PNG.
- [var destinationRect: CGRect](scscreenshotconfiguration/destinationrect.md)
  A rectangle that specifies whether to output screenshots in a subset of the output image.
- [var displayIntent: SCScreenshotConfiguration.DisplayIntent](scscreenshotconfiguration/displayintent-swift.property.md)
  Specifies whether the screen capture uses attributes of the local or canonical display.
- [var dynamicRange: SCScreenshotConfiguration.DynamicRange](scscreenshotconfiguration/dynamicrange-swift.property.md)
  Specifies the type of image returned to the client; standard dynamic range, high dynamic range, or both.
- [var fileURL: URL?](scscreenshotconfiguration/fileurl.md)
  Specifies the URL where the screenshot process saves the output.
- [var height: Int](scscreenshotconfiguration/height.md)
  An integer value that specifies the output height, measured in pixels.
- [var ignoreClipping: Bool](scscreenshotconfiguration/ignoreclipping.md)
  A Boolean value that specifies whether to ignore framing on windows when using content filters.
- [var ignoreShadows: Bool](scscreenshotconfiguration/ignoreshadows.md)
  A Boolean value that specifies whether to ignore framing on windows.
- [var includeChildWindows: Bool](scscreenshotconfiguration/includechildwindows.md)
  A Boolean that specifies whether the screenshot captures subwindows of the included apps and windows.
- [var showsCursor: Bool](scscreenshotconfiguration/showscursor.md)
  A Boolean value that specifies whether the pointer appears in the screenshot.
- [var sourceRect: CGRect](scscreenshotconfiguration/sourcerect.md)
  A rectangle that specifies that the screenshot only samples a subset of the frame input.
- [var width: Int](scscreenshotconfiguration/width.md)
  An integer value that specifies the output width in pixels.
### Type Properties
- [class var supportedContentTypes: [UTType]](scscreenshotconfiguration/supportedcontenttypes.md)
  An array of uniform type identifiers that correspond to file formats the output image supports.
### Enumerations
- [SCScreenshotConfiguration.DisplayIntent](scscreenshotconfiguration/displayintent-swift.enum.md)
  A value that specifies the type of display a screenshot rendering optimizes for.
- [SCScreenshotConfiguration.DynamicRange](scscreenshotconfiguration/dynamicrange-swift.enum.md)
  Specifies the type of images returned to the client; standard dynamic range, high dynamic range, or both.

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
- [class SCScreenshotManager](scscreenshotmanager.md)
  An instance for the capture of single frames from a stream.
- [class SCScreenshotOutput](scscreenshotoutput.md)
  An object that contains all images requested by the client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration)*