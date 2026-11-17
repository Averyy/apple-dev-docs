# CPLaneStatus

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

Values that describe the status or preferability of a lane.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum CPLaneStatus
```

```c
enum CPLaneStatus : NSInteger;
```

## Topics

### Getting the lane status
- [CPLaneStatus.notGood](./cplanestatus/notgood.md)
  The lane status is not good.
- [CPLaneStatus.good](./cplanestatus/good.md)
  The lane status is good.
- [CPLaneStatus.preferred](./cplanestatus/preferred.md)
  The lane status is preferred.
### Creating a lane status
- [init?(rawValue: Int)](./cplanestatus/init%28rawvalue%29.md)
  Creates a lane status with the provided value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Lanes and junctions
- [class CPLane](./cplane.md)
  A class that describes characteristics of a lane on a roadway.
- [class CPLaneGuidance](./cplaneguidance.md)
  A class that provides information that describes the number of lanes on a roadway and navigation instruction variants.
- [enum CPJunctionType](./cpjunctiontype.md)
  Values that represent types of roadway junctions.
- [enum CPTrafficSide](./cptrafficside.md)
  Values that represent which side of the road the traffic drives on.
- [func NSStringFromCPJunctionType(CPJunctionType) -> String!](./nsstringfromcpjunctiontype%28_%29.md)
- [func NSStringFromCPLaneStatus(CPLaneStatus) -> String!](./nsstringfromcplanestatus%28_%29.md)
- [func NSStringFromCPTrafficSide(CPTrafficSide) -> String!](./nsstringfromcptrafficside%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplanestatus)*