# SCStreamFrameInfo

**Framework**: ScreenCaptureKit  
**Kind**: struct

An instance that defines metadata keys for a stream frame.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
struct SCStreamFrameInfo
```

#### Overview

Use [`SCStreamFrameInfo`](scstreamframeinfo.md) keys to retrieve values from the dictionary of metadata attached to the sample buffers that a stream produces. For example, you can retrieve the display time, content scale, and scaling factor, as shown below:

```swift
// A dictionary of attachments for a streamed sample buffer.
let attachments: [SCStreamFrameInfo: Any] = // Retrieve attachments from a sample buffer.

let displayTime = attachments[.displayTime] as? UInt64 ?? 0
let contentScale = attachments[.contentScale] as? Double ?? 0.0
let scaleFactor = attachments[.scaleFactor] as? Double ?? 0.0
```

## Topics

### Frame information constants
- [static let status: SCStreamFrameInfo](scstreamframeinfo/status.md)
  A key to retrieve the status of a video frame.
- [static let displayTime: SCStreamFrameInfo](scstreamframeinfo/displaytime.md)
  A key to retrieve the display time of a video frame.
- [static let scaleFactor: SCStreamFrameInfo](scstreamframeinfo/scalefactor.md)
  A key to retrieve the scale factor of a video frame.
- [static let contentScale: SCStreamFrameInfo](scstreamframeinfo/contentscale.md)
  A key to retrieve the content scale of a video frame.
- [static let contentRect: SCStreamFrameInfo](scstreamframeinfo/contentrect.md)
  A key to retrieve the content rectangle of a video frame.
- [static let boundingRect: SCStreamFrameInfo](scstreamframeinfo/boundingrect.md)
  A key to retrieve the bounding rectangle for a video frame.
- [static let screenRect: SCStreamFrameInfo](scstreamframeinfo/screenrect.md)
  A key to retrieve the onscreen location of captured content.
- [static let dirtyRects: SCStreamFrameInfo](scstreamframeinfo/dirtyrects.md)
  A key to retrieve the areas of a video frame that contain changes.
- [static let presenterOverlayContentRect: SCStreamFrameInfo](scstreamframeinfo/presenteroverlaycontentrect.md)
### Initializers
- [init(rawValue: String)](scstreamframeinfo/init(rawvalue:).md)
  Creates a new instance with a raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol SCStreamOutput](scstreamoutput.md)
  A delegate protocol your app implements to receive capture stream output events.
- [enum SCStreamOutputType](scstreamoutputtype.md)
  Constants that represent output types for a stream frame.
- [enum SCFrameStatus](scframestatus.md)
  Status values for a frame from a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamframeinfo)*