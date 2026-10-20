# dirtyRects

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Type Property

A key to retrieve the areas of a video frame that contain changes.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
static let dirtyRects: SCStreamFrameInfo
```

```c
extern SCStreamFrameInfo const SCStreamFrameInfoDirtyRects;
```

#### Discussion

The associated value is an array of rectangles that represents a union of the rectangles redrawn and moved.

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
- [static let boundingRect: SCStreamFrameInfo](./boundingrect.md)
  A key to retrieve the bounding rectangle for a video frame.
- [static let screenRect: SCStreamFrameInfo](./screenrect.md)
  A key to retrieve the onscreen location of captured content.
- [static let presenterOverlayContentRect: SCStreamFrameInfo](./presenteroverlaycontentrect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamframeinfo/dirtyrects)*