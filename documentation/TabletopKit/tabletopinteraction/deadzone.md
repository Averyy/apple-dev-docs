# TabletopInteraction.DeadZone

**Framework**: TabletopKit  
**Kind**: enum  
**Role**: Enumeration

The dead zone allows to specify how much the input device should move or rotate from its initial pose to start moving the object.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum DeadZone
```

## Topics

### Interaction zones
- [TabletopInteraction.DeadZone.default](./deadzone/default.md)
  The default dead zone values.
- [TabletopInteraction.DeadZone.disabled](./deadzone/disabled.md)
  Use this value to disable the dead zone.
- [TabletopInteraction.DeadZone.within(distance:angle:)](./deadzone/within%28distance,angle%29.md)
  Allows to customize the dead zone values. The object will start moving when the first of these two thresholds is reached.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/deadzone)*