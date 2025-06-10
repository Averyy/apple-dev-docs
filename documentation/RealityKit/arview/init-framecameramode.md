# init(frame:cameraMode:)

**Framework**: RealityKit  
**Kind**: init

Creates an AR view with the specified dimensions and camera mode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- Unknown ?+ - Deprecated

## Declaration

```swift
@MainActor
@preconcurrency convenience init(frame frameRect: CGRect, cameraMode: ARView.CameraMode)
```

## Parameters

- `frameRect`: The frame rectangle for the view, measured in points.
- `cameraMode`: An indication of whether to use the device’s camera or   a virtual one.

## See Also

- [init(frame: CGRect)](arview/init(frame:).md)
  Creates an AR view with the specified dimensions.
- [init(frame: CGRect, cameraMode: ARView.CameraMode, automaticallyConfigureSession: Bool)](arview/init(frame:cameramode:automaticallyconfiguresession:).md)
  Creates an AR view with the specified dimensions, camera mode, and session configuration state.
- [init?(coder: NSCoder)](arview/init(coder:).md)
  Creates an AR view initialized from data in a given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/init(frame:cameramode:))*