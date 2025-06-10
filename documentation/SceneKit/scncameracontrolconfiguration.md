# SCNCameraControlConfiguration

**Framework**: SceneKit  
**Kind**: protocol

Properties affecting the behavior of a camera controller.

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
protocol SCNCameraControlConfiguration : NSObjectProtocol
```

## Topics

### Instance Properties
- [var allowsTranslation: Bool](scncameracontrolconfiguration/allowstranslation.md)
- [var autoSwitchToFreeCamera: Bool](scncameracontrolconfiguration/autoswitchtofreecamera.md)
- [var flyModeVelocity: CGFloat](scncameracontrolconfiguration/flymodevelocity.md)
- [var panSensitivity: CGFloat](scncameracontrolconfiguration/pansensitivity.md)
- [var rotationSensitivity: CGFloat](scncameracontrolconfiguration/rotationsensitivity.md)
- [var truckSensitivity: CGFloat](scncameracontrolconfiguration/trucksensitivity.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var allowsCameraControl: Bool](scnview/allowscameracontrol.md)
  A Boolean value that determines whether the user can manipulate the current point of view that is used to render the scene.
- [var cameraControlConfiguration: any SCNCameraControlConfiguration](scnview/cameracontrolconfiguration.md)
  The current configuration for the camera controller’s event-handling behavior.
- [var defaultCameraController: SCNCameraController](scnview/defaultcameracontroller.md)
- [class SCNCameraController](scncameracontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncameracontrolconfiguration)*