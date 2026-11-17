# CPTrafficSide

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

Values that represent which side of the road the traffic drives on.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum CPTrafficSide
```

```c
enum CPTrafficSide : NSUInteger;
```

## Topics

### Getting the traffic side
- [CPTrafficSide.right](./cptrafficside/right.md)
  Indicates the traffic drives on the right side of the roadway.
- [CPTrafficSide.left](./cptrafficside/left.md)
  Indicates the traffic drives on the left side of the roadway.
### Creating a traffic side
- [init?(rawValue: UInt)](./cptrafficside/init%28rawvalue%29.md)
  Creates a traffic side-of-the-road enumeration item with the provided value.

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
- [enum CPJunctionType](./cpjunctiontype.md)
  Values that represent types of roadway junctions.
- [func NSStringFromCPJunctionType(CPJunctionType) -> String!](./nsstringfromcpjunctiontype%28_%29.md)
- [func NSStringFromCPLaneStatus(CPLaneStatus) -> String!](./nsstringfromcplanestatus%28_%29.md)
- [func NSStringFromCPTrafficSide(CPTrafficSide) -> String!](./nsstringfromcptrafficside%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptrafficside)*