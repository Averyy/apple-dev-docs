# junctionElementAngles

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A set of angles for the rest of the roads of this junction.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var junctionElementAngles: Set<Measurement<UnitAngle>>? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSSet<NSMeasurement<NSUnitAngle *> *> * junctionElementAngles;
```

### Discussion

This must not include `junctionExitAngle`.

## See Also

### Providing junction information
- [var junctionType: CPJunctionType](./junctiontype.md)
  A value that represents the type of junction associated with this maneuver.
- [var junctionExitAngle: Measurement<UnitAngle>?](./junctionexitangle.md)
  The angle of the exit road of this junction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/junctionelementangles)*