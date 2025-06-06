# junctionType

**Framework**: CarPlay  
**Kind**: property

A value that represents the type of junction associated with this maneuver.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var junctionType: CPJunctionType { get set }
```

#### Discussion

One of the [`CPJunctionType`](cpjunctiontype.md) values that indicates the type of traffic junction; a [`CPManeuver`](cpmaneuver.md) requires this value.

## See Also

- [var junctionExitAngle: Measurement<UnitAngle>?](cpmaneuver/junctionexitangle.md)
  The angle of the exit road of this junction.
- [var junctionElementAngles: Set<Measurement<UnitAngle>>?](cpmaneuver/junctionelementangles.md)
  A set of angles for the rest of the roads of this junction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/junctiontype)*