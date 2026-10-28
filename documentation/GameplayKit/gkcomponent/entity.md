# entity

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, weak, readonly, nullable) GKEntity * entity;
```

## Discussion

Use this property in a component subclass to refer back to the owning entity and its attributes. An entity may be an instance either of the [`GKEntity`](../gkentity.md) class or of a custom subclass. In the latter case, a custom entity class can provide storage for state or resources accessed by multiple components.

## See Also

### Working with Entities
- [func didAddToEntity()](./didaddtoentity%28%29.md)
  Notifies the component that it has been assigned to an entity.
- [func willRemoveFromEntity()](./willremovefromentity%28%29.md)
  Notifies the component that it has been removed from an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponent/entity)*