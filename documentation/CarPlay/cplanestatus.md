# CPLaneStatus

**Framework**: CarPlay  
**Kind**: enum

Values that describe the status or preferability of a lane.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum CPLaneStatus
```

## Topics

### Initializers
- [init?(rawValue: Int)](cplanestatus/init(rawvalue:).md)
  Creates a lane status with the provided value.
### Lane statuses
- [CPLaneStatus.notGood](cplanestatus/notgood.md)
  The lane status is not good.
- [CPLaneStatus.good](cplanestatus/good.md)
  The lane status is good.
- [CPLaneStatus.preferred](cplanestatus/preferred.md)
  The lane status is preferred.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CPRouteInformation](cprouteinformation.md)
  A class that describes the characteristic elements of a route.
- [class CPLane](cplane.md)
  A class that describes characteristics of a lane on a roadway.
- [class CPLaneGuidance](cplaneguidance.md)
  A class that provides information that describes the number of lanes on a roadway and navigation instruction variants.
- [enum CPJunctionType](cpjunctiontype.md)
  Values that represent types of roadway junctions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplanestatus)*