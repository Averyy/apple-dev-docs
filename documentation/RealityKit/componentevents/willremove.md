# ComponentEvents.WillRemove

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Event raised before a component is removed from an entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct WillRemove
```

## Topics

### Instance Properties
- [let componentType: any Component.Type](./willremove/componenttype.md)
  The component type.
- [let entity: Entity](./willremove/entity.md)
  The component’s entity.

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Detecting component changes
- [ComponentEvents.DidAdd](./didadd.md)
  Event raised after a component has been added to an entity,
- [ComponentEvents.DidChange](./didchange.md)
  Event raised after a component has been modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/componentevents/willremove)*