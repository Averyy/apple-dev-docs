# TabletopInteraction.Configuration

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- visionOS 2.2+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init()](./configuration/init%28%29.md)
- [init(allowedDestinations: TabletopInteraction.AllowedDestinations)](./configuration/init%28alloweddestinations%29.md)
- [init(allowedDestinations: TabletopInteraction.AllowedDestinations, hoverAlignment: TabletopInteraction.HoverAlignmentBehavior)](./configuration/init%28alloweddestinations,hoveralignment%29.md)
### Getting the allowed destinations
- [var allowedDestinations: TabletopInteraction.AllowedDestinations](./configuration/alloweddestinations.md)
  The set of equipment that are allowed to be proposed as potential parents of the one being controlled.
### Getting the hover alignment
- [var hoverAlignment: TabletopInteraction.HoverAlignmentBehavior](./configuration/hoveralignment.md)
  Hover alignment describes how the equipment should behave when hovering a target.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the interaction destination
- [func setConfiguration(TabletopInteraction.Configuration)](./setconfiguration%28_%29.md)
  Sets the configuration of this interaction.
- [TabletopInteraction.AllowedDestinations](./alloweddestinations.md)
  The possible destinations of equipment in an interaction.
- [TabletopInteraction.Destination](./destination.md)
  An object that represents the destination position and orientation of equipment in an interaction.
- [func setAllowedDestinations(TabletopInteraction.AllowedDestinations)](./setalloweddestinations%28_%29.md)
  Sets which equipment the interaction can target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/configuration)*