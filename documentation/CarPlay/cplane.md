# CPLane

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A class that describes characteristics of a lane on a roadway.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
class CPLane
```

```objc
@interface CPLane : NSObject
```

## Topics

### Properties
- [var primaryAngle: Measurement<UnitAngle>](./cplane/primaryangle.md)
  A value that represents the angle the framework highlights if this lane is preferred or good.
- [var secondaryAngles: [Measurement<UnitAngle>]](./cplane/secondaryangles.md)
  A list of the remaining angles of this lane guidance.
- [var status: CPLaneStatus](./cplane/status.md)
  A value that describes the lane’s status.
### Lane status
- [enum CPLaneStatus](./cplanestatus.md)
  Values that describe the status or preferability of a lane.
### Initializers
- [init()](./cplane/init%28%29.md)
- [init(angles: [Measurement<UnitAngle>])](./cplane/init%28angles%29.md)
- [init(angles: [Measurement<UnitAngle>], highlightedAngle: Measurement<UnitAngle>, isPreferred: Bool)](./cplane/init%28angles,highlightedangle,ispreferred%29.md)
- [init?(coder: NSCoder)](./cplane/init%28coder%29.md)
### Instance Properties
- [var angles: [Measurement<UnitAngle>]](./cplane/angles.md)
- [var highlightedAngle: Measurement<UnitAngle>?](./cplane/highlightedangle.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Routes, lanes and junctions
- [class CPRouteInformation](./cprouteinformation.md)
  A class that describes the characteristic elements of a route.
- [class CPLaneGuidance](./cplaneguidance.md)
  A class that provides information that describes the number of lanes on a roadway and navigation instruction variants.
- [enum CPLaneStatus](./cplanestatus.md)
  Values that describe the status or preferability of a lane.
- [enum CPJunctionType](./cpjunctiontype.md)
  Values that represent types of roadway junctions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplane)*