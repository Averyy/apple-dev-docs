# allowsCameraControl

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the user can manipulate the current point of view that is used to render the scene.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var allowsCameraControl: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsCameraControl;
```

#### Discussion

If you set this property to [`true`](../../Swift/true.md), SceneKit creates a camera node and handles mouse or touch events to allow the user to pan, zoom, and rotate their view of the scene. (Enabling user camera control does not modify camera objects already existing in the scene graph or the nodes containing them.)

When you enable user camera control, the [`defaultCameraController`](./defaultcameracontroller.md) object handles input events and drives camera behavior. You can use that object’s methods and properties to change the style of user camera interaction, and use the [`cameraControlConfiguration`](./cameracontrolconfiguration.md) property to adjust control sensitivity.

In the default configuration, SceneKit provides the following controls:

- Pan with one finger to rotate the camera around the scene
- Pan with two fingers to translate the camera on its local xy-plane
- Pan with three fingers vertically to move the camera forward and backward
- Double-tap to switch to the next camera in the scene
- Rotate with two fingers to roll the camera (rotate on the camera node’s z-axis)
- Pinch to zoom in or zoom out (change the camera’s [`fieldOfView`](../scncamera/fieldofview.md))

The default value of this property is [`false`](../../Swift/false.md). Use this option if you intend to control the camera programmatically.

## See Also

### Managing Camera Controls
- [var cameraControlConfiguration: any SCNCameraControlConfiguration](./cameracontrolconfiguration.md)
  The current configuration for the camera controller’s event-handling behavior.
- [protocol SCNCameraControlConfiguration](../scncameracontrolconfiguration.md)
  Properties affecting the behavior of a camera controller.
- [var defaultCameraController: SCNCameraController](./defaultcameracontroller.md)
- [class SCNCameraController](../scncameracontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/allowscameracontrol)*