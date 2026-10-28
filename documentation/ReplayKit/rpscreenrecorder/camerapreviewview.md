# cameraPreviewView

**Framework**: ReplayKit  
**Kind**: property  
**Role**: Instance Property

A view containing the contents of the front-facing camera.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use ScreenCaptureKit SCVideoEffectOutput instead

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
var cameraPreviewView: UIView? { get }
```

*macOS*

```swift
var cameraPreviewView: NSView? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly, nullable) UIView * cameraPreviewView;
```

*macOS*

```objc
@property (nonatomic, readonly, nullable) NSView * cameraPreviewView;
```

## Discussion

When the value in the [`isCameraEnabled`](./iscameraenabled.md) property is [`true`](../../Swift/true.md), this property contains a view with the live camera view. If the camera isn’t enabled, the value in this property is `nil`. When the app runs in visionOS, the value in this property is `nil`.

## See Also

### Inspecting a Screen Recorder
- [var isAvailable: Bool](./isavailable.md)
  A Boolean value that indicates whether the screen recorder is available for recording.
- [var isRecording: Bool](./isrecording.md)
  A Boolean value that indicates whether the app is currently recording.
- [var isMicrophoneEnabled: Bool](./ismicrophoneenabled.md)
  A Boolean value that indicates whether the microphone is currently enabled.
- [var isCameraEnabled: Bool](./iscameraenabled.md)
  A Boolean value that indicates whether the camera is currently enabled.
- [var cameraPosition: RPCameraPosition](./cameraposition.md)
  The camera position to use.
- [enum RPCameraPosition](../rpcameraposition.md)
  The position of the camera being accessed.
- [var delegate: (any RPScreenRecorderDelegate)?](./delegate.md)
  The delegate for the screen recorder.
- [protocol RPScreenRecorderDelegate](../rpscreenrecorderdelegate.md)
  The protocol you implement to receive notifications from the screen recorder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/camerapreviewview)*