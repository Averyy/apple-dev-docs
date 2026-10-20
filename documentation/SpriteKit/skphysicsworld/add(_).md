# add(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Adds a joint to the physics world.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func add(_ joint: SKPhysicsJoint)
```

```objc
- (void) addJoint:(SKPhysicsJoint *) joint;
```

## Mentions

- [Connecting Bodies with Joints](../connecting-bodies-with-joints.md)

#### Discussion

For a joint to take effect, it must be added to the physics world.

## Parameters

- `joint`: The joint to add.

## See Also

### Joining Physics Bodies with Joints
- [func removeAllJoints()](./removealljoints%28%29.md)
  Removes all joints from the physics world.
- [func remove(SKPhysicsJoint)](./remove%28_%29.md)
  Removes a specific joint from the physics world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsworld/add(_:))*