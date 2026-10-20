# ComponentEvents.DidAdd

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Event raised after a component has been added to an entity,

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct DidAdd
```

## Topics

### Instance Properties
- [let componentType: any Component.Type](./didadd/componenttype.md)
  The component type.
- [let entity: Entity](./didadd/entity.md)
  The component’s entity.

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Detecting component changes
- [ComponentEvents.DidChange](./didchange.md)
  Event raised after a component has been modified.
- [ComponentEvents.WillRemove](./willremove.md)
  Event raised before a component is removed from an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/componentevents/didadd)*