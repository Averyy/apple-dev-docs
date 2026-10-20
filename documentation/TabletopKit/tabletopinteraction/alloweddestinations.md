# TabletopInteraction.AllowedDestinations

**Framework**: TabletopKit  
**Kind**: enum  
**Role**: Enumeration

The possible destinations of equipment in an interaction.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
enum AllowedDestinations
```

## Topics

### Destinations
- [TabletopInteraction.AllowedDestinations.any](./alloweddestinations/any.md)
  Any equipment is allowed to be the proposed destination
- [TabletopInteraction.AllowedDestinations.restricted(_:)](./alloweddestinations/restricted%28_%29.md)
  Restricts the proposed destination to the given identifiers

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the interaction destination
- [func setConfiguration(TabletopInteraction.Configuration)](./setconfiguration%28_%29.md)
  Sets the configuration of this interaction.
- [TabletopInteraction.Configuration](./configuration.md)
- [TabletopInteraction.Destination](./destination.md)
  An object that represents the destination position and orientation of equipment in an interaction.
- [func setAllowedDestinations(TabletopInteraction.AllowedDestinations)](./setalloweddestinations%28_%29.md)
  Sets which equipment the interaction can target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/alloweddestinations)*