# displayTime

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Type Property

A key to retrieve the display time of a video frame.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static let displayTime: SCStreamFrameInfo
```

```c
extern SCStreamFrameInfo const SCStreamFrameInfoDisplayTime;
```

#### Discussion

For a frame event, this value represents the time the window server displays the frame.

## See Also

### Frame information constants
- [static let status: SCStreamFrameInfo](./status.md)
  A key to retrieve the status of a video frame.
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
- [static let dirtyRects: SCStreamFrameInfo](./dirtyrects.md)
  A key to retrieve the areas of a video frame that contain changes.
- [static let presenterOverlayContentRect: SCStreamFrameInfo](./presenteroverlaycontentrect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamframeinfo/displaytime)*