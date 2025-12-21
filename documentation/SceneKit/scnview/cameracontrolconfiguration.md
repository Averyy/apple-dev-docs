# cameraControlConfiguration

**Framework**: SceneKit  
**Kind**: property

The current configuration for the camera controller’s event-handling behavior.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@MainActor
var cameraControlConfiguration: any SCNCameraControlConfiguration { get }
```

## See Also

- [var allowsCameraControl: Bool](scnview/allowscameracontrol.md)
  A Boolean value that determines whether the user can manipulate the current point of view that is used to render the scene.
- [protocol SCNCameraControlConfiguration](scncameracontrolconfiguration.md)
  Properties affecting the behavior of a camera controller.
- [var defaultCameraController: SCNCameraController](scnview/defaultcameracontroller.md)
- [class SCNCameraController](scncameracontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/cameracontrolconfiguration)*