# AVCaptureViewDelegate

**Framework**: AVKit  
**Kind**: protocol

The protocol that defines the methods you can implement to respond to capture view events.

**Availability**:
- macOS 10.9+

## Declaration

```swift
protocol AVCaptureViewDelegate : NSObjectProtocol
```

## Topics

### Starting a New Recording
- [func captureView(AVCaptureView, startRecordingTo: AVCaptureFileOutput)](avcaptureviewdelegate/captureview(_:startrecordingto:).md)
  Tells the delegate that the user has made a request to start a new recording.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any AVCaptureViewDelegate)?](avcaptureview/delegate.md)
  The capture view’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureviewdelegate)*