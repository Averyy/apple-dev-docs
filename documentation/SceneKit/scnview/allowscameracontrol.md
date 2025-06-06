# allowsCameraControl

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether the user can manipulate the current point of view that is used to render the scene.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var allowsCameraControl: Bool { get set }
```

#### Discussion

If you set this property to [`true`](https://developer.apple.com/documentation/swift/true), SceneKit creates a camera node and handles mouse or touch events to allow the user to pan, zoom, and rotate their view of the scene. (Enabling user camera control does not modify camera objects already existing in the scene graph or the nodes containing them.)

When you enable user camera control, the [`defaultCameraController`](scnview/defaultcameracontroller.md) object handles input events and drives camera behavior. You can use that object’s methods and properties to change the style of user camera interaction, and use the [`cameraControlConfiguration`](scnview/cameracontrolconfiguration.md) property to adjust control sensitivity.

In the default configuration, SceneKit provides the following controls:

- Pan with one finger to rotate the camera around the scene
- Pan with two fingers to translate the camera on its local xy-plane
- Pan with three fingers vertically to move the camera forward and backward
- Double-tap to switch to the next camera in the scene
- Rotate with two fingers to roll the camera (rotate on the camera node’s z-axis)
- Pinch to zoom in or zoom out (change the camera’s [`fieldOfView`](scncamera/fieldofview.md))

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false). Use this option if you intend to control the camera programmatically.

## See Also

- [var cameraControlConfiguration: any SCNCameraControlConfiguration](scnview/cameracontrolconfiguration.md)
  The current configuration for the camera controller’s event-handling behavior.
- [protocol SCNCameraControlConfiguration](scncameracontrolconfiguration.md)
  Properties affecting the behavior of a camera controller.
- [var defaultCameraController: SCNCameraController](scnview/defaultcameracontroller.md)
- [class SCNCameraController](scncameracontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/allowscameracontrol)*