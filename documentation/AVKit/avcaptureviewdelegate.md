# AVCaptureViewDelegate

**Framework**: AVKit  
**Kind**: protocol  
**Role**: Protocol

The protocol that defines the methods you can implement to respond to capture view events.

**Availability**:
- macOS 10.9+

## Declaration

```swift
protocol AVCaptureViewDelegate : NSObjectProtocol
```

```objc
@protocol AVCaptureViewDelegate <NSObject>
```

## Topics

### Starting a new recording
- [func captureView(AVCaptureView, startRecordingTo: AVCaptureFileOutput)](./avcaptureviewdelegate/captureview%28_,startrecordingto%29.md)
  Tells the delegate that the user has made a request to start a new recording.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Capture views
- [class AVCaptureView](./avcaptureview.md)
  A view that displays standard user interface controls for capturing media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureviewdelegate)*