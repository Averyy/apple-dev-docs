# didAddToEntity()

**Framework**: GameplayKit  
**Kind**: method

Notifies the component that it has been assigned to an entity.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func didAddToEntity()
```

#### Discussion

Override this method in a component subclass if you need to perform game logic when the component is added to an entity. For example, if one component’s behavior depends on the presence of other components in the same entity, you can examine the entity’s [`components`](gkentity/components.md) array in this method and take action accordingly.

## See Also

- [var entity: GKEntity?](gkcomponent/entity.md)
  The entity that owns this component.
- [func willRemoveFromEntity()](gkcomponent/willremovefromentity.md)
  Notifies the component that it has been removed from an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponent/didaddtoentity())*