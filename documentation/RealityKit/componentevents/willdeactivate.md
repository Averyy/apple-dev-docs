# ComponentEvents.WillDeactivate

**Framework**: RealityKit  
**Kind**: struct

Event raised before a component is deactivated.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct WillDeactivate
```

## Topics

### Instance Properties
- [let componentType: any Component.Type](componentevents/willdeactivate/componenttype.md)
  The component type.
- [let entity: Entity](componentevents/willdeactivate/entity.md)
  The component’s entity.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [ComponentEvents.DidActivate](componentevents/didactivate.md)
  Event raised after a component has been activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/componentevents/willdeactivate)*