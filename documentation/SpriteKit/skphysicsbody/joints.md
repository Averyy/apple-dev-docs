# joints

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The joints connected to this physics body.

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
var joints: [SKPhysicsJoint] { get }
```

```objc
@property (nonatomic, readonly) NSArray<SKPhysicsJoint *> * joints;
```

## Discussion

This property holds an array of [`SKPhysicsJoint`](../skphysicsjoint.md) objects that define all joints added to the scene’s physics world that are connected to this physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/joints)*