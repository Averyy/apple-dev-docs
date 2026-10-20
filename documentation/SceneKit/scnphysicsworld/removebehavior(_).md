# removeBehavior(_:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Removes a behavior from the physics world.

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
func removeBehavior(_ behavior: SCNPhysicsBehavior)
```

```objc
- (void) removeBehavior:(SCNPhysicsBehavior *) behavior;
```

## Parameters

- `behavior`: The behavior to be removed.

## See Also

### Registering Physics Behaviors
- [func addBehavior(SCNPhysicsBehavior)](./addbehavior%28_%29.md)
  Adds a behavior to the physics world.
- [var allBehaviors: [SCNPhysicsBehavior]](./allbehaviors.md)
  The list of behaviors affecting bodies in the physics world.
- [func removeAllBehaviors()](./removeallbehaviors%28%29.md)
  Removes all behaviors affecting bodies in the physics world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/removebehavior(_:))*