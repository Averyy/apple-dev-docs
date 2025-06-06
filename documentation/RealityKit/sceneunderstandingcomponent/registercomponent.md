# registerComponent()

**Framework**: RealityKit  
**Kind**: method

Registers a new component type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
static func registerComponent()
```

#### Discussion

Call the `registerComponent()` method once for every custom component type that you use in your app before you use it. You don’t need to call the method for built-in component types, like [`ModelComponent`](modelcomponent.md) or [`AnchoringComponent`](anchoringcomponent.md).

## See Also

- [var entityType: SceneUnderstandingComponent.EntityType?](sceneunderstandingcomponent/entitytype-swift.property.md)
  The type of real-world objects that the component models.
- [SceneUnderstandingComponent.EntityType](sceneunderstandingcomponent/entitytype-swift.enum.md)
  Types of real-world objects that a scene-understanding component models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneunderstandingcomponent/registercomponent())*