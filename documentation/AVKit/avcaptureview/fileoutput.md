# fileOutput

**Framework**: AVKit  
**Kind**: property

The capture file output used to record media data.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var fileOutput: AVCaptureFileOutput? { get }
```

#### Discussion

The value of this property is the first capture file output object contained in the session’s [`outputs`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/outputs) array, or `nil` if it has no outputs. In the latter case, the capture view disables the start recording button. However, it may still enable the controls for choosing input sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureview/fileoutput)*