# AVCaptureScreenInput

**Framework**: AVFoundation  
**Kind**: class

A capture input for recording from a screen in macOS.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class AVCaptureScreenInput
```

#### Overview

> ❗ **Important**:  Starting in macOS 12.3, use the [`ScreenCaptureKit`](https://developer.apple.com/documentation/ScreenCaptureKit) framework for screen recording instead.

This class is a concrete capture input subclass that provides an interface to capture media from a screen or a portion of a screen.

Use instances of this class as input sources for [`AVCaptureSession`](avcapturesession.md) objects that provide media data from one of the screens connected to the system, represented by [`CGDirectDisplayID`](https://developer.apple.com/documentation/CoreGraphics/CGDirectDisplayID).

## Topics

### Initializing a Capture Screen Input
- [init?(displayID: CGDirectDisplayID)](avcapturescreeninput/init(displayid:).md)
  Initializes a capture screen input that provides media data from the specified display.
- [init()](avcapturescreeninput/init.md)
  Initializes a capture screen input that provides media data from the main screen.
### Setting Video Capture Options
- [var minFrameDuration: CMTime](avcapturescreeninput/minframeduration.md)
  The screen input’s minimum frame duration.
- [var cropRect: CGRect](avcapturescreeninput/croprect.md)
  Indicates the bounding rectangle of the screen area to be captured, in pixels.
- [var scaleFactor: CGFloat](avcapturescreeninput/scalefactor.md)
  Indicates the factor by which video buffers captured from the screen are to be scaled.
### Capturing Mouse Activity
- [var capturesCursor: Bool](avcapturescreeninput/capturescursor.md)
  A Boolean value that specifies whether the mouse cursor appears in the captured output.
- [var capturesMouseClicks: Bool](avcapturescreeninput/capturesmouseclicks.md)
  A Boolean value that specifies whether mouse clicks appear highlighted in the captured output.
### Deprecated
- [var removesDuplicateFrames: Bool](avcapturescreeninput/removesduplicateframes.md)
  A Boolean value that specifies whether the capture input skips duplicate frames.

## Relationships

### Inherits From
- [AVCaptureInput](avcaptureinput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput)*