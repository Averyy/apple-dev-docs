# RPCameraPosition

**Framework**: ReplayKit  
**Kind**: enum

The position of the camera being accessed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum RPCameraPosition
```

## Topics

### Enumeration Cases
- [RPCameraPosition.back](rpcameraposition/back.md)
  The back camera is used.
- [RPCameraPosition.front](rpcameraposition/front.md)
  The front camera is used.
### Initializers
- [init?(rawValue: Int)](rpcameraposition/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](rpcameraposition/equatable-implementations.md)
- [RawRepresentable Implementations](rpcameraposition/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isAvailable: Bool](rpscreenrecorder/isavailable.md)
  A Boolean value that indicates whether the screen recorder is available for recording.
- [var isRecording: Bool](rpscreenrecorder/isrecording.md)
  A Boolean value that indicates whether the app is currently recording.
- [var isMicrophoneEnabled: Bool](rpscreenrecorder/ismicrophoneenabled.md)
  A Boolean value that indicates whether the microphone is currently enabled.
- [var isCameraEnabled: Bool](rpscreenrecorder/iscameraenabled.md)
  A Boolean value that indicates whether the camera is currently enabled.
- [var cameraPreviewView: UIView?](rpscreenrecorder/camerapreviewview.md)
  A view containing the contents of the front-facing camera.
- [var cameraPosition: RPCameraPosition](rpscreenrecorder/cameraposition.md)
  The camera position to use.
- [var delegate: (any RPScreenRecorderDelegate)?](rpscreenrecorder/delegate.md)
  The delegate for the screen recorder.
- [protocol RPScreenRecorderDelegate](rpscreenrecorderdelegate.md)
  The protocol you implement to receive notifications from the screen recorder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpcameraposition)*