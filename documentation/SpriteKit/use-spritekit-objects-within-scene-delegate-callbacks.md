# Use SpriteKit Objects within Scene Delegate Callbacks

**Framework**: Spritekit

Follow threading guidelines to keep your SpriteKit app thread safe.

#### Overview

SpriteKit is largely a single threaded game engine and as such the API provides developers with callbacks to implement your custom game logic. The primary callback for your game logic is [`update(_:for:)`](skscenedelegate/update(_:for:).md). Other callbacks are illustrated in [`SKSceneDelegate`](skscenedelegate.md). Modifying SpriteKit objects outside of the scene delegate callbacks (such as in a background queue or anything else not running on the main thread) can result in concurrency related problems. Even dispatching work on the main thread asynchronously or at a later time is risky because the closure is likely to be done outside of the timeframe SpriteKit expects. If you’re experiencing a segmentation fault or other type of crash occurring deep within the SpriteKit framework, there’s a good chance your code is modifying a SpriteKit object outside of the scene delegate callbacks.

> **Note**:  To check at runtime if a particular block of code is running on the main thread, inspect [`isMainThread`](https://developer.apple.com/documentation/foundation/thread/1408455-ismainthread).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/SpriteKit/use-spritekit-objects-within-scene-delegate-callbacks)*