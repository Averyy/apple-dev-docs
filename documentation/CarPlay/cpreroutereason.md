# CPRerouteReason

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

Values that represent reasons for navigation rerouting.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
enum CPRerouteReason
```

```c
enum CPRerouteReason : NSInteger;
```

## Topics

### Getting the reroute reason
- [CPRerouteReason.alternateRoute](./cpreroutereason/alternateroute.md)
  A value that represents rerouting because an alternate route became available.
- [CPRerouteReason.missedTurn](./cpreroutereason/missedturn.md)
  A value that represents rerouting because of a missed turn.
- [CPRerouteReason.offline](./cpreroutereason/offline.md)
  A value that represents rerouting because the system was offline.
- [CPRerouteReason.mandated](./cpreroutereason/mandated.md)
  A reroute was required due to external circumstances, such as a road closure.
- [CPRerouteReason.waypointModified](./cpreroutereason/waypointmodified.md)
  An existing waypoint was modified or updated.
- [CPRerouteReason.unknown](./cpreroutereason/unknown.md)
  The reason for rerouting is unknown or not specified.
### Initializers
- [init?(rawValue: Int)](./cpreroutereason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Route details
- [class CPRouteChoice](./cproutechoice.md)
  A possible route for a trip.
- [class CPRouteInformation](./cprouteinformation.md)
  A class that describes the characteristic elements of a route.
- [class CPRouteDetail](./cproutedetail.md)
- [class CPRouteSegment](./cproutesegment.md)
  CPRouteSegment describes information pertaining to a segment of a route.
- [enum CPRouteSource](./cproutesource.md)
- [func NSStringFromCPRerouteReason(CPRerouteReason) -> String!](./nsstringfromcpreroutereason%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpreroutereason)*