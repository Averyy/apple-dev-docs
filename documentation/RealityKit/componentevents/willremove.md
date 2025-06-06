# ComponentEvents.WillRemove

**Framework**: RealityKit  
**Kind**: struct

Event raised before a component is removed from an entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct WillRemove
```

## Topics

### Instance Properties
- [let componentType: any Component.Type](componentevents/willremove/componenttype.md)
  The component type.
- [let entity: Entity](componentevents/willremove/entity.md)
  The component’s entity.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [ComponentEvents.DidAdd](componentevents/didadd.md)
  Event raised after a component has been added to an entity,
- [ComponentEvents.DidChange](componentevents/didchange.md)
  Event raised after a component has been modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/componentevents/willremove)*