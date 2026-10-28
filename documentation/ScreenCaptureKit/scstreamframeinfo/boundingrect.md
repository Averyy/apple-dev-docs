# boundingRect

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Type Property

A key to retrieve the bounding rectangle for a video frame.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
static let boundingRect: SCStreamFrameInfo
```

```c
extern SCStreamFrameInfo const SCStreamFrameInfoBoundingRect;
```

## Discussion

The bounding rectangle provided for a frame is the minimum bounding box for containing all captured windows in the frame.

## See Also

### Frame information constants
- [static let status: SCStreamFrameInfo](./status.md)
  A key to retrieve the status of a video frame.
- [static let displayTime: SCStreamFrameInfo](./displaytime.md)
  A key to retrieve the display time of a video frame.
- [static let scaleFactor: SCStreamFrameInfo](./scalefactor.md)
  A key to retrieve the scale factor of a video frame.
- [static let contentScale: SCStreamFrameInfo](./contentscale.md)
  A key to retrieve the content scale of a video frame.
- [static let contentRect: SCStreamFrameInfo](./contentrect.md)
  A key to retrieve the content rectangle of a video frame.
- [static let screenRect: SCStreamFrameInfo](./screenrect.md)
  A key to retrieve the onscreen location of captured content.
- [static let dirtyRects: SCStreamFrameInfo](./dirtyrects.md)
  A key to retrieve the areas of a video frame that contain changes.
- [static let presenterOverlayContentRect: SCStreamFrameInfo](./presenteroverlaycontentrect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamframeinfo/boundingrect)*