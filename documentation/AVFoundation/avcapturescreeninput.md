# AVCaptureScreenInput

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

A capture input for recording from a screen in macOS.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class AVCaptureScreenInput
```

```objc
@interface AVCaptureScreenInput : AVCaptureInput
```

## Overview

> ❗ **Important**:  Starting in macOS 12.3, use the [ScreenCaptureKit](../ScreenCaptureKit/ScreenCaptureKit.md) framework for screen recording instead.

This class is a concrete capture input subclass that provides an interface to capture media from a screen or a portion of a screen.

Use instances of this class as input sources for [`AVCaptureSession`](./avcapturesession.md) objects that provide media data from one of the screens connected to the system, represented by [`CGDirectDisplayID`](../CoreGraphics/cgdirectdisplayid.md).

## Topics

### Initializing a capture screen input
- [init?(displayID: CGDirectDisplayID)](./avcapturescreeninput/init%28displayid%29.md)
  Initializes a capture screen input that provides media data from the specified display.
- [init()](./avcapturescreeninput/init%28%29.md)
  Initializes a capture screen input that provides media data from the main screen.
- [+ new](./avcapturescreeninput/new.md)
  Creates a capture screen input that provides media data from the main screen.
### Setting video capture options
- [var minFrameDuration: CMTime](./avcapturescreeninput/minframeduration.md)
  The screen input’s minimum frame duration.
- [var cropRect: CGRect](./avcapturescreeninput/croprect.md)
  Indicates the bounding rectangle of the screen area to be captured, in pixels.
- [var scaleFactor: CGFloat](./avcapturescreeninput/scalefactor.md)
  Indicates the factor by which video buffers captured from the screen are to be scaled.
### Capturing mouse activity
- [var capturesCursor: Bool](./avcapturescreeninput/capturescursor.md)
  A Boolean value that specifies whether the mouse cursor appears in the captured output.
- [var capturesMouseClicks: Bool](./avcapturescreeninput/capturesmouseclicks.md)
  A Boolean value that specifies whether mouse clicks appear highlighted in the captured output.
### Deprecated
- [var removesDuplicateFrames: Bool](./avcapturescreeninput/removesduplicateframes.md)
  A Boolean value that specifies whether the capture input skips duplicate frames.

## Relationships

### Inherits From
- [AVCaptureInput](./avcaptureinput.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput)*