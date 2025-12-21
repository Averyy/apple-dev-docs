# ComponentEvents.DidChange

**Framework**: RealityKit  
**Kind**: struct

Event raised after a component has been modified.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct DidChange
```

## Topics

### Instance Properties
- [let componentType: any Component.Type](componentevents/didchange/componenttype.md)
  The component type.
- [let entity: Entity](componentevents/didchange/entity.md)
  The component’s entity.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ComponentEvents.DidAdd](componentevents/didadd.md)
  Event raised after a component has been added to an entity,
- [ComponentEvents.WillRemove](componentevents/willremove.md)
  Event raised before a component is removed from an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/componentevents/didchange)*