# CPJunctionType

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

Values that represent types of roadway junctions.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum CPJunctionType
```

```c
enum CPJunctionType : NSUInteger;
```

## Topics

### Getting the junction types
- [CPJunctionType.intersection](./cpjunctiontype/intersection.md)
  A single intersection with roads coming to a common point.
- [CPJunctionType.roundabout](./cpjunctiontype/roundabout.md)
  Junction elements that represent roads exiting the roundabout.
### Creating a junction type
- [init?(rawValue: UInt)](./cpjunctiontype/init%28rawvalue%29.md)
  Creates a junction type with the provided integer value.

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
- [enum CPLaneStatus](./cplanestatus.md)
  Values that describe the status or preferability of a lane.
- [enum CPTrafficSide](./cptrafficside.md)
  Values that represent which side of the road the traffic drives on.
- [func NSStringFromCPJunctionType(CPJunctionType) -> String!](./nsstringfromcpjunctiontype%28_%29.md)
- [func NSStringFromCPLaneStatus(CPLaneStatus) -> String!](./nsstringfromcplanestatus%28_%29.md)
- [func NSStringFromCPTrafficSide(CPTrafficSide) -> String!](./nsstringfromcptrafficside%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpjunctiontype)*