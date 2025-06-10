# TabletopInteraction.AllowedDestinations

**Framework**: TabletopKit  
**Kind**: enum

The possible destinations of equipment in an interaction.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
enum AllowedDestinations
```

## Topics

### Destinations
- [TabletopInteraction.AllowedDestinations.any](tabletopinteraction/alloweddestinations/any.md)
  Any equipment is allowed to be the proposed destination
- [TabletopInteraction.AllowedDestinations.restricted(_:)](tabletopinteraction/alloweddestinations/restricted(_:).md)
  Restricts the proposed destination to the given identifiers

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setAllowedDestinations(TabletopInteraction.AllowedDestinations)](tabletopinteraction/setalloweddestinations(_:).md)
  Sets which equipment the interaction can target.
- [TabletopInteraction.Destination](tabletopinteraction/destination.md)
  An object that represents the destination position and orientation of equipment in an interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/alloweddestinations)*