# init(frame:cameraMode:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates an AR view with the specified dimensions and camera mode.

**Availability**:
- iOS 13.0+ - Deprecated (renamed: init(frame:cameraMode:automaticallyConfigureSession:))
- iPadOS 13.0+ - Deprecated (renamed: init(frame:cameraMode:automaticallyConfigureSession:))
- Mac Catalyst 14.0+ - Deprecated (renamed: init(frame:cameraMode:automaticallyConfigureSession:))

## Declaration

```swift
@MainActor
@preconcurrency convenience init(frame frameRect: CGRect, cameraMode: ARView.CameraMode)
```

## Parameters

- `frameRect`: The frame rectangle for the view, measured in points.
- `cameraMode`: An indication of whether to use the device’s camera or a virtual one.

## See Also

### Creating a view
- [init(frame: CGRect)](./init%28frame%29.md)
  Creates an AR view with the specified dimensions.
- [init(frame: CGRect, cameraMode: ARView.CameraMode, automaticallyConfigureSession: Bool)](./init%28frame,cameramode,automaticallyconfiguresession%29.md)
  Creates an AR view with the specified dimensions, camera mode, and session configuration state.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates an AR view initialized from data in a given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/init(frame:cameramode:))*