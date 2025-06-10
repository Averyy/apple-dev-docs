# init(frame:)

**Framework**: RealityKit  
**Kind**: init

Creates an AR view with the specified dimensions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency override required dynamic init(frame frameRect: NSRect)
```

## Parameters

- `frameRect`: The frame rectangle for the view, measured in points.

## See Also

- [init(frame: CGRect, cameraMode: ARView.CameraMode, automaticallyConfigureSession: Bool)](arview/init(frame:cameramode:automaticallyconfiguresession:).md)
  Creates an AR view with the specified dimensions, camera mode, and session configuration state.
- [init?(coder: NSCoder)](arview/init(coder:).md)
  Creates an AR view initialized from data in a given decoder.
- [convenience init(frame: CGRect, cameraMode: ARView.CameraMode)](arview/init(frame:cameramode:).md)
  Creates an AR view with the specified dimensions and camera mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/init(frame:))*