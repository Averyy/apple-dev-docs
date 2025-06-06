# SceneUnderstandingComponent.EntityType

**Framework**: RealityKit  
**Kind**: enum

Types of real-world objects that a scene-understanding component models.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
enum EntityType
```

## Topics

### Choosing the entity type
- [SceneUnderstandingComponent.EntityType.face](sceneunderstandingcomponent/entitytype-swift.enum/face.md)
  An entity that models a face that the framework detects in the physical environment.
- [SceneUnderstandingComponent.EntityType.meshChunk](sceneunderstandingcomponent/entitytype-swift.enum/meshchunk.md)
  An entity that models the physical shape of the environment within a given cubic region.
### Comparing entity types
- [static func == (SceneUnderstandingComponent.EntityType, SceneUnderstandingComponent.EntityType) -> Bool](sceneunderstandingcomponent/entitytype-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](sceneunderstandingcomponent/entitytype-swift.enum/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](sceneunderstandingcomponent/entitytype-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](sceneunderstandingcomponent/entitytype-swift.enum/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](sceneunderstandingcomponent/entitytype-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var entityType: SceneUnderstandingComponent.EntityType?](sceneunderstandingcomponent/entitytype-swift.property.md)
  The type of real-world objects that the component models.
- [static func registerComponent()](sceneunderstandingcomponent/registercomponent.md)
  Registers a new component type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneunderstandingcomponent/entitytype-swift.enum)*