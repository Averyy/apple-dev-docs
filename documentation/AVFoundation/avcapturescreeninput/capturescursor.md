# capturesCursor

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that specifies whether the mouse cursor appears in the captured output.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var capturesCursor: Bool { get set }
```

#### Discussion

When this property is true (the default), captured video frames include the mouse pointer. If you change this property to false, the captured output contains only the windows on the screen (that is, the mouse pointer is invisible in captured video).

> **Note**:  Even if you hide the mouse pointer in captured output, [`CMSampleBuffer`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer) objects vended by the capture include metadata for the cursor position and mouse button state. See [`kCMIOSampleBufferAttachmentKey_MouseAndKeyboardModifiers`](https://developer.apple.com/documentation/CoreMediaIO/kCMIOSampleBufferAttachmentKey_MouseAndKeyboardModifiers).

## See Also

- [var capturesMouseClicks: Bool](avcapturescreeninput/capturesmouseclicks.md)
  A Boolean value that specifies whether mouse clicks appear highlighted in the captured output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/capturescursor)*