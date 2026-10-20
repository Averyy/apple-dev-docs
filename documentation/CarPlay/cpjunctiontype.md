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

### Initializers
- [init?(rawValue: UInt)](./cpjunctiontype/init%28rawvalue%29.md)
  Creates a junction type with the provided integer value.
### Junction types
- [CPJunctionType.intersection](./cpjunctiontype/intersection.md)
  A single intersection with roads coming to a common point.
- [CPJunctionType.roundabout](./cpjunctiontype/roundabout.md)
  Junction elements that represent roads exiting the roundabout.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Routes, lanes and junctions
- [class CPRouteInformation](./cprouteinformation.md)
  A class that describes the characteristic elements of a route.
- [class CPLane](./cplane.md)
  A class that describes characteristics of a lane on a roadway.
- [class CPLaneGuidance](./cplaneguidance.md)
  A class that provides information that describes the number of lanes on a roadway and navigation instruction variants.
- [enum CPLaneStatus](./cplanestatus.md)
  Values that describe the status or preferability of a lane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpjunctiontype)*