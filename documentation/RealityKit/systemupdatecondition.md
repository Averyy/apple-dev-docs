# SystemUpdateCondition

**Framework**: RealityKit  
**Kind**: struct

A condition which causes a system to update.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct SystemUpdateCondition
```

## Topics

### Type Properties
- [static var rendering: SystemUpdateCondition](systemupdatecondition/rendering.md)
  A condition that is active whenever an update for rendering may be needed, usually matching the refresh rate of the display.

## See Also

- [Implementing systems for entities in a scene](implementing-systems-for-entities-in-a-scene.md)
  Apply behaviors and physical effects to the objects and characters in a RealityKit scene with the Entity Component System (ECS).
- [protocol System](system.md)
  An object that affects multiple entities in every update of a RealityKit scene.
- [struct SceneUpdateContext](sceneupdatecontext.md)
  An object that contains information about the scene to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/systemupdatecondition)*