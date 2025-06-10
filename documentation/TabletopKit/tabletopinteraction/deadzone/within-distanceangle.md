# TabletopInteraction.DeadZone.within(distance:angle:)

**Framework**: TabletopKit  
**Kind**: case

Allows to customize the dead zone values. The object will start moving when the first of these two thresholds is reached.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
case within(distance: Double, angle: Angle2D)
```

## Parameters

- `distance`: The minimum amount of distance that the input device should move from its initial position.
- `angle`: The minimum angle that the device should rotate from its initial orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/deadzone/within(distance:angle:))*