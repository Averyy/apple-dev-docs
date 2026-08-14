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

> ❗ **Important**:  Starting in macOS 12.3, use the [`ScreenCaptureKit`](https://developer.apple.com/documentation/screencapturekit) framework for screen recording instead.

This class is a concrete capture input subclass that provides an interface to capture media from a screen or a portion of a screen.

Use instances of this class as input sources for [`AVCaptureSession`](avcapturesession.md) objects that provide media data from one of the screens connected to the system, represented by [`CGDirectDisplayID`](https://developer.apple.com/documentation/coregraphics/cgdirectdisplayid).

## Topics

### Initializing a capture screen input
- [init?(displayID: CGDirectDisplayID)](avcapturescreeninput/init(displayid:).md)
  Initializes a capture screen input that provides media data from the specified display.
- [init()](avcapturescreeninput/init.md)
  Initializes a capture screen input that provides media data from the main screen.
### Setting video capture options
- [var minFrameDuration: CMTime](avcapturescreeninput/minframeduration.md)
  The screen input’s minimum frame duration.
- [var cropRect: CGRect](avcapturescreeninput/croprect.md)
  Indicates the bounding rectangle of the screen area to be captured, in pixels.
- [var scaleFactor: CGFloat](avcapturescreeninput/scalefactor.md)
  Indicates the factor by which video buffers captured from the screen are to be scaled.
### Capturing mouse activity
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
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput)*