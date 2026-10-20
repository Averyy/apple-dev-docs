# capturesCursor

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether the mouse cursor appears in the captured output.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var capturesCursor: Bool { get set }
```

```objc
@property (nonatomic) BOOL capturesCursor;
```

#### Discussion

When this property is true (the default), captured video frames include the mouse pointer. If you change this property to false, the captured output contains only the windows on the screen (that is, the mouse pointer is invisible in captured video).

> **Note**:  Even if you hide the mouse pointer in captured output, [`CMSampleBuffer`](../../CoreMedia/cmsamplebuffer.md) objects vended by the capture include metadata for the cursor position and mouse button state. See [`kCMIOSampleBufferAttachmentKey_MouseAndKeyboardModifiers`](../../CoreMediaIO/kcmiosamplebufferattachmentkey_mouseandkeyboardmodifiers.md).

## See Also

### Capturing mouse activity
- [var capturesMouseClicks: Bool](./capturesmouseclicks.md)
  A Boolean value that specifies whether mouse clicks appear highlighted in the captured output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/capturescursor)*