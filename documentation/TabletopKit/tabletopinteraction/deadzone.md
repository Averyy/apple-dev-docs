# TabletopInteraction.DeadZone

**Framework**: TabletopKit  
**Kind**: enum

The dead zone allows to specify how much the input device should move or rotate from its initial pose to start moving the object.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum DeadZone
```

## Topics

### Enumeration Cases
- [TabletopInteraction.DeadZone.default](tabletopinteraction/deadzone/default.md)
  The default dead zone values.
- [TabletopInteraction.DeadZone.disabled](tabletopinteraction/deadzone/disabled.md)
  Use this value to disable the dead zone.
- [TabletopInteraction.DeadZone.within(distance:angle:)](tabletopinteraction/deadzone/within(distance:angle:).md)
  Allows to customize the dead zone values. The object will start moving when the first of these two thresholds is reached.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/deadzone)*