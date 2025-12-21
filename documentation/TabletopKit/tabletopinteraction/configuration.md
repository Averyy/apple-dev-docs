# TabletopInteraction.Configuration

**Framework**: TabletopKit  
**Kind**: struct

**Availability**:
- visionOS 2.2+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init()](tabletopinteraction/configuration/init.md)
- [init(allowedDestinations: TabletopInteraction.AllowedDestinations)](tabletopinteraction/configuration/init(alloweddestinations:).md)
- [init(allowedDestinations: TabletopInteraction.AllowedDestinations, hoverAlignment: TabletopInteraction.HoverAlignmentBehavior)](tabletopinteraction/configuration/init(alloweddestinations:hoveralignment:).md)
### Getting the allowed destinations
- [var allowedDestinations: TabletopInteraction.AllowedDestinations](tabletopinteraction/configuration/alloweddestinations.md)
  The set of equipment that are allowed to be proposed as potential parents of the one being controlled.
### Getting the hover alignment
- [var hoverAlignment: TabletopInteraction.HoverAlignmentBehavior](tabletopinteraction/configuration/hoveralignment.md)
  Hover alignment describes how the equipment should behave when hovering a target.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setConfiguration(TabletopInteraction.Configuration)](tabletopinteraction/setconfiguration(_:).md)
  Sets the configuration of this interaction.
- [TabletopInteraction.AllowedDestinations](tabletopinteraction/alloweddestinations.md)
  The possible destinations of equipment in an interaction.
- [TabletopInteraction.Destination](tabletopinteraction/destination.md)
  An object that represents the destination position and orientation of equipment in an interaction.
- [func setAllowedDestinations(TabletopInteraction.AllowedDestinations)](tabletopinteraction/setalloweddestinations(_:).md)
  Sets which equipment the interaction can target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/configuration)*