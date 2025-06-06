# CPLane

**Framework**: CarPlay  
**Kind**: class

A class that describes characteristics of a lane on a roadway.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
class CPLane
```

## Topics

### Properties
- [var primaryAngle: Measurement<UnitAngle>](cplane/primaryangle.md)
  A value that represents the angle the framework highlights if this lane is preferred or good.
- [var secondaryAngles: [Measurement<UnitAngle>]](cplane/secondaryangles.md)
  A list of the remaining angles of this lane guidance.
- [var status: CPLaneStatus](cplane/status.md)
  A value that describes the lane’s status.
### Lane status
- [enum CPLaneStatus](cplanestatus.md)
  Values that describe the status or preferability of a lane.
### Initializers
- [init()](cplane/init.md)
- [init(angles: [Measurement<UnitAngle>])](cplane/init(angles:).md)
- [init(angles: [Measurement<UnitAngle>], highlightedAngle: Measurement<UnitAngle>, isPreferred: Bool)](cplane/init(angles:highlightedangle:ispreferred:).md)
### Instance Properties
- [var angles: [Measurement<UnitAngle>]](cplane/angles.md)
- [var highlightedAngle: Measurement<UnitAngle>?](cplane/highlightedangle.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CPRouteInformation](cprouteinformation.md)
  A class that describes the characteristic elements of a route.
- [class CPLaneGuidance](cplaneguidance.md)
  A class that provides information that describes the number of lanes on a roadway and navigation instruction variants.
- [enum CPLaneStatus](cplanestatus.md)
  Values that describe the status or preferability of a lane.
- [enum CPJunctionType](cpjunctiontype.md)
  Values that represent types of roadway junctions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplane)*