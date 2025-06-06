# boundingRect

**Framework**: ScreenCaptureKit  
**Kind**: property

A key to retrieve the bounding rectangle for a video frame.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
static let boundingRect: SCStreamFrameInfo
```

#### Discussion

The bounding rectangle provided for a frame is the minimum bounding box for containing all captured windows in the frame.

## See Also

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
- [static let screenRect: SCStreamFrameInfo](scstreamframeinfo/screenrect.md)
  A key to retrieve the onscreen location of captured content.
- [static let dirtyRects: SCStreamFrameInfo](scstreamframeinfo/dirtyrects.md)
  A key to retrieve the areas of a video frame that contain changes.
- [static let presenterOverlayContentRect: SCStreamFrameInfo](scstreamframeinfo/presenteroverlaycontentrect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamframeinfo/boundingrect)*