# SCScreenshotConfiguration

**Framework**: ScreenCaptureKit  
**Kind**: class

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
class SCScreenshotConfiguration
```

## Topics

### Instance Properties
- [var contentType: UTTypeReference](scscreenshotconfiguration/contenttype.md)
- [var destinationRect: CGRect](scscreenshotconfiguration/destinationrect.md)
- [var displayIntent: SCScreenshotConfiguration.DisplayIntent](scscreenshotconfiguration/displayintent-swift.property.md)
- [var dynamicRange: SCScreenshotConfiguration.DynamicRange](scscreenshotconfiguration/dynamicrange-swift.property.md)
- [var fileURL: URL?](scscreenshotconfiguration/fileurl.md)
- [var height: Int](scscreenshotconfiguration/height.md)
- [var ignoreClipping: Bool](scscreenshotconfiguration/ignoreclipping.md)
- [var ignoreShadows: Bool](scscreenshotconfiguration/ignoreshadows.md)
- [var includeChildWindows: Bool](scscreenshotconfiguration/includechildwindows.md)
- [var showsCursor: Bool](scscreenshotconfiguration/showscursor.md)
- [var sourceRect: CGRect](scscreenshotconfiguration/sourcerect.md)
- [var width: Int](scscreenshotconfiguration/width.md)
### Type Properties
- [class var supportedContentTypes: [UTType]](scscreenshotconfiguration/supportedcontenttypes.md)
### Enumerations
- [SCScreenshotConfiguration.DisplayIntent](scscreenshotconfiguration/displayintent-swift.enum.md)
- [SCScreenshotConfiguration.DynamicRange](scscreenshotconfiguration/dynamicrange-swift.enum.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration)*