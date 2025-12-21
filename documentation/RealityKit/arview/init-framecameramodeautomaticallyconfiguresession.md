# init(frame:cameraMode:automaticallyConfigureSession:)

**Framework**: RealityKit  
**Kind**: init

Creates an AR view with the specified dimensions, camera mode, and session configuration state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
@preconcurrency init(frame frameRect: CGRect, cameraMode: ARView.CameraMode, automaticallyConfigureSession: Bool)
```

## Parameters

- `frameRect`: The frame rectangle for the view, measured in points.
- `cameraMode`: An indication of whether to use the device’s camera or   a virtual one.
- `automaticallyConfigureSession`: An indication of whether to use an   AR session with configuration that’s updated automatically based on   camera mode and scene anchors. Set this value to   if you want   to run the session manually with your own configuration.

## See Also

- [init(frame: CGRect)](arview/init(frame:).md)
  Creates an AR view with the specified dimensions.
- [init?(coder: NSCoder)](arview/init(coder:).md)
  Creates an AR view initialized from data in a given decoder.
- [convenience init(frame: CGRect, cameraMode: ARView.CameraMode)](arview/init(frame:cameramode:).md)
  Creates an AR view with the specified dimensions and camera mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/init(frame:cameramode:automaticallyconfiguresession:))*