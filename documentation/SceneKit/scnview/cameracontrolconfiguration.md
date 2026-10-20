# cameraControlConfiguration

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The current configuration for the camera controller’s event-handling behavior.

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
var cameraControlConfiguration: any SCNCameraControlConfiguration { get }
```

```objc
@property (nonatomic, readonly) id<SCNCameraControlConfiguration> cameraControlConfiguration;
```

## See Also

### Managing Camera Controls
- [var allowsCameraControl: Bool](./allowscameracontrol.md)
  A Boolean value that determines whether the user can manipulate the current point of view that is used to render the scene.
- [protocol SCNCameraControlConfiguration](../scncameracontrolconfiguration.md)
  Properties affecting the behavior of a camera controller.
- [var defaultCameraController: SCNCameraController](./defaultcameracontroller.md)
- [class SCNCameraController](../scncameracontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/cameracontrolconfiguration)*