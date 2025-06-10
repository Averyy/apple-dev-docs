# SCNCameraController

**Framework**: SceneKit  
**Kind**: class

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
class SCNCameraController
```

## Topics

### Responding to Control Events
- [var delegate: (any SCNCameraControllerDelegate)?](scncameracontroller/delegate.md)
- [protocol SCNCameraControllerDelegate](scncameracontrollerdelegate.md)
### Supporting Types
- [enum SCNInteractionMode](scninteractionmode.md)
### Instance Properties
- [var automaticTarget: Bool](scncameracontroller/automatictarget.md)
- [var inertiaEnabled: Bool](scncameracontroller/inertiaenabled.md)
- [var inertiaFriction: Float](scncameracontroller/inertiafriction.md)
- [var interactionMode: SCNInteractionMode](scncameracontroller/interactionmode.md)
- [var isInertiaRunning: Bool](scncameracontroller/isinertiarunning.md)
- [var maximumHorizontalAngle: Float](scncameracontroller/maximumhorizontalangle.md)
- [var maximumVerticalAngle: Float](scncameracontroller/maximumverticalangle.md)
- [var minimumHorizontalAngle: Float](scncameracontroller/minimumhorizontalangle.md)
- [var minimumVerticalAngle: Float](scncameracontroller/minimumverticalangle.md)
- [var pointOfView: SCNNode?](scncameracontroller/pointofview.md)
- [var target: SCNVector3](scncameracontroller/target.md)
- [var worldUp: SCNVector3](scncameracontroller/worldup.md)
### Instance Methods
- [func beginInteraction(CGPoint, withViewport: CGSize)](scncameracontroller/begininteraction(_:withviewport:).md)
- [func clearRoll()](scncameracontroller/clearroll.md)
- [func continueInteraction(CGPoint, withViewport: CGSize, sensitivity: CGFloat)](scncameracontroller/continueinteraction(_:withviewport:sensitivity:).md)
- [func dolly(by: Float, onScreenPoint: CGPoint, viewport: CGSize)](scncameracontroller/dolly(by:onscreenpoint:viewport:).md)
- [func dolly(toTarget: Float)](scncameracontroller/dolly(totarget:).md)
- [func endInteraction(CGPoint, withViewport: CGSize, velocity: CGPoint)](scncameracontroller/endinteraction(_:withviewport:velocity:).md)
- [func frameNodes([SCNNode])](scncameracontroller/framenodes(_:).md)
- [func roll(by: Float, aroundScreenPoint: CGPoint, viewport: CGSize)](scncameracontroller/roll(by:aroundscreenpoint:viewport:).md)
- [func rollAroundTarget(Float)](scncameracontroller/rollaroundtarget(_:).md)
- [func rotateBy(x: Float, y: Float)](scncameracontroller/rotateby(x:y:).md)
- [func stopInertia()](scncameracontroller/stopinertia.md)
- [func translateInCameraSpaceBy(x: Float, y: Float, z: Float)](scncameracontroller/translateincameraspaceby(x:y:z:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var allowsCameraControl: Bool](scnview/allowscameracontrol.md)
  A Boolean value that determines whether the user can manipulate the current point of view that is used to render the scene.
- [var cameraControlConfiguration: any SCNCameraControlConfiguration](scnview/cameracontrolconfiguration.md)
  The current configuration for the camera controller’s event-handling behavior.
- [protocol SCNCameraControlConfiguration](scncameracontrolconfiguration.md)
  Properties affecting the behavior of a camera controller.
- [var defaultCameraController: SCNCameraController](scnview/defaultcameracontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncameracontroller)*