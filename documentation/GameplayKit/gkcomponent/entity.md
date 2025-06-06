# entity

**Framework**: GameplayKit  
**Kind**: property

The entity that owns this component.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
weak var entity: GKEntity? { get }
```

#### Discussion

Use this property in a component subclass to refer back to the owning entity and its attributes. An entity may be an instance either of the [`GKEntity`](gkentity.md) class or of a custom subclass. In the latter case, a custom entity class can provide storage for state or resources accessed by multiple components.

## See Also

- [func didAddToEntity()](gkcomponent/didaddtoentity.md)
  Notifies the component that it has been assigned to an entity.
- [func willRemoveFromEntity()](gkcomponent/willremovefromentity.md)
  Notifies the component that it has been removed from an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponent/entity)*