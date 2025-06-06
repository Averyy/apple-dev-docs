# junctionElementAngles

**Framework**: CarPlay  
**Kind**: property

A set of angles for the rest of the roads of this junction.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var junctionElementAngles: Set<Measurement<UnitAngle>>? { get set }
```

##### Discussion

This must not include `junctionExitAngle`.

## See Also

- [var junctionType: CPJunctionType](cpmaneuver/junctiontype.md)
  A value that represents the type of junction associated with this maneuver.
- [var junctionExitAngle: Measurement<UnitAngle>?](cpmaneuver/junctionexitangle.md)
  The angle of the exit road of this junction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/junctionelementangles)*