# SCNCameraController

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

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
class SCNCameraController
```

```objc
@interface SCNCameraController : NSObject
```

## Topics

### Responding to Control Events
- [var delegate: (any SCNCameraControllerDelegate)?](./scncameracontroller/delegate.md)
- [protocol SCNCameraControllerDelegate](./scncameracontrollerdelegate.md)
### Supporting Types
- [enum SCNInteractionMode](./scninteractionmode.md)
### Instance Properties
- [var automaticTarget: Bool](./scncameracontroller/automatictarget.md)
- [var inertiaEnabled: Bool](./scncameracontroller/inertiaenabled.md)
- [var inertiaFriction: Float](./scncameracontroller/inertiafriction.md)
- [var interactionMode: SCNInteractionMode](./scncameracontroller/interactionmode.md)
- [var isInertiaRunning: Bool](./scncameracontroller/isinertiarunning.md)
- [var maximumHorizontalAngle: Float](./scncameracontroller/maximumhorizontalangle.md)
- [var maximumVerticalAngle: Float](./scncameracontroller/maximumverticalangle.md)
- [var minimumHorizontalAngle: Float](./scncameracontroller/minimumhorizontalangle.md)
- [var minimumVerticalAngle: Float](./scncameracontroller/minimumverticalangle.md)
- [var pointOfView: SCNNode?](./scncameracontroller/pointofview.md)
- [var target: SCNVector3](./scncameracontroller/target.md)
- [var worldUp: SCNVector3](./scncameracontroller/worldup.md)
### Instance Methods
- [func beginInteraction(CGPoint, withViewport: CGSize)](./scncameracontroller/begininteraction%28_,withviewport%29.md)
- [func clearRoll()](./scncameracontroller/clearroll%28%29.md)
- [func continueInteraction(CGPoint, withViewport: CGSize, sensitivity: CGFloat)](./scncameracontroller/continueinteraction%28_,withviewport,sensitivity%29.md)
- [func dolly(by: Float, onScreenPoint: CGPoint, viewport: CGSize)](./scncameracontroller/dolly%28by,onscreenpoint,viewport%29.md)
- [func dolly(toTarget: Float)](./scncameracontroller/dolly%28totarget%29.md)
- [func endInteraction(CGPoint, withViewport: CGSize, velocity: CGPoint)](./scncameracontroller/endinteraction%28_,withviewport,velocity%29.md)
- [func frameNodes([SCNNode])](./scncameracontroller/framenodes%28_%29.md)
- [func roll(by: Float, aroundScreenPoint: CGPoint, viewport: CGSize)](./scncameracontroller/roll%28by,aroundscreenpoint,viewport%29.md)
- [func rollAroundTarget(Float)](./scncameracontroller/rollaroundtarget%28_%29.md)
- [func rotateBy(x: Float, y: Float)](./scncameracontroller/rotateby%28x,y%29.md)
- [func stopInertia()](./scncameracontroller/stopinertia%28%29.md)
- [func translateInCameraSpaceBy(x: Float, y: Float, z: Float)](./scncameracontroller/translateincameraspaceby%28x,y,z%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Managing Camera Controls
- [var allowsCameraControl: Bool](./scnview/allowscameracontrol.md)
  A Boolean value that determines whether the user can manipulate the current point of view that is used to render the scene.
- [var cameraControlConfiguration: any SCNCameraControlConfiguration](./scnview/cameracontrolconfiguration.md)
  The current configuration for the camera controller’s event-handling behavior.
- [protocol SCNCameraControlConfiguration](./scncameracontrolconfiguration.md)
  Properties affecting the behavior of a camera controller.
- [var defaultCameraController: SCNCameraController](./scnview/defaultcameracontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncameracontroller)*