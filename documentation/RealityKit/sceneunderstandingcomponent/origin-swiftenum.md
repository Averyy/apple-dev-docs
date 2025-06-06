# SceneUnderstandingComponent.Origin

**Framework**: RealityKit  
**Kind**: enum

Types of scene-understanding origins this component lives in.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum Origin
```

## Topics

### Operators
- [static func == (SceneUnderstandingComponent.Origin, SceneUnderstandingComponent.Origin) -> Bool](sceneunderstandingcomponent/origin-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [SceneUnderstandingComponent.Origin.system](sceneunderstandingcomponent/origin-swift.enum/system.md)
  A scene-understanding component that is owned and created by the system. Component of this origin type will model an object in real world environment.
- [SceneUnderstandingComponent.Origin.user](sceneunderstandingcomponent/origin-swift.enum/user.md)
  A scene-understanding component that is owned and created by the developer. Component of this origin type will model an object in virtual environment.
### Instance Properties
- [var hashValue: Int](sceneunderstandingcomponent/origin-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](sceneunderstandingcomponent/origin-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](sceneunderstandingcomponent/origin-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneunderstandingcomponent/origin-swift.enum)*