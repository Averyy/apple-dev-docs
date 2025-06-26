# SKSceneDelegate

**Framework**: SpriteKit  
**Kind**: protocol

Methods that, when implemented, allow any class to participate in the SpriteKit render loop callbacks.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
protocol SKSceneDelegate : NSObjectProtocol
```

## Mentions

- [Getting Started with Nodes](getting-started-with-nodes.md)
- [Detecting Changes at Each Step of an Animation](detecting-changes-at-each-step-of-an-animation.md)
- [Getting Started with Actions](getting-started-with-actions.md)
- [Displaying 3D Content in a SpriteKit Scene](displaying-3d-content-in-a-spritekit-scene.md)
- [Subclassing Scenes Versus Assigning a Delegate](subclassing-scenes-versus-assigning-a-delegate.md)
- [Use SpriteKit Objects within Scene Delegate Callbacks](use-spritekit-objects-within-scene-delegate-callbacks.md)
- [Disconnecting Bodies from Joints](disconnecting-bodies-from-joints.md)
- [Configuring a Physics Body](configuring-a-physics-body.md)
- [Responding to Frame-Cycle Events](responding-to-frame-cycle-events.md)

#### Overview

The [`SKSceneDelegate`](skscenedelegate.md) protocol is used to implement a delegate to be called whenever the scene is being animated. Typically, you supply a delegate when you want to use a scene without requiring the scene to be subclassed. The methods in this protocol all correspond to methods implemented by the [`SKScene`](skscene.md) class. If the delegate implements a particular method, that method is called instead of the corresponding method on the scene object.

When processing a scene, SpriteKit runs a loop that processes and renders the scene. The [`SKSceneDelegate`](skscenedelegate.md) methods allows you to add logic at any step of the loop.

![Frame processing in a scene](https://docs-assets.developer.apple.com/published/be1a33d8b82e5a33a9f3873c756bb121/media-2527821%402x.png)

> ❗ **Important**:  If your view has a [`SKViewDelegate`](skviewdelegate.md) and its [`view(_:shouldRenderAtTime:)`](skviewdelegate/view(_:shouldrenderattime:).md) method returns [`false`](https://developer.apple.com/documentation/swift/false), the update is skipped and none of the scene delegate methods are called.

## Topics

### Handling Animation Events
- [Use SpriteKit Objects within Scene Delegate Callbacks](use-spritekit-objects-within-scene-delegate-callbacks.md)
  Follow threading guidelines to keep your SpriteKit app thread safe.
- [func update(TimeInterval, for: SKScene)](skscenedelegate/update(_:for:).md)
  Tells you to perform any app specific logic to update your scene.
- [func didEvaluateActions(for: SKScene)](skscenedelegate/didevaluateactions(for:).md)
  Tells you to peform any necessary logic after scene actions are evaluated.
- [func didSimulatePhysics(for: SKScene)](skscenedelegate/didsimulatephysics(for:).md)
  Tells you to peform any necessary logic after physics simulations are performed.
- [func didApplyConstraints(for: SKScene)](skscenedelegate/didapplyconstraints(for:).md)
  Tells you to peform any necessary logic after constraints are applied.
- [func didFinishUpdate(for: SKScene)](skscenedelegate/didfinishupdate(for:).md)
  Tells you to peform any necessary logic after the scene has finished all of the steps required to process animations.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Subclassing Scenes Versus Assigning a Delegate](subclassing-scenes-versus-assigning-a-delegate.md)
  Use a scene delegate to share app logic across various scenes.
- [var delegate: (any SKSceneDelegate)?](skscene/delegate.md)
  A delegate to be called during the animation loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscenedelegate)*