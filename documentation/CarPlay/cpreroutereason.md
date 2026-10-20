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

### Properties
- [CPRerouteReason.alternateRoute](./cpreroutereason/alternateroute.md)
  A value that represents rerouting because an alternate route became available.
- [CPRerouteReason.missedTurn](./cpreroutereason/missedturn.md)
  A value that represents rerouting because of a missed turn.
- [CPRerouteReason.offline](./cpreroutereason/offline.md)
  A value that represents rerouting because the system was offline.
### Enumeration Cases
- [CPRerouteReason.mandated](./cpreroutereason/mandated.md)
  A reroute was required due to external circumstances, such as a road closure.
- [CPRerouteReason.unknown](./cpreroutereason/unknown.md)
  The reason for rerouting is unknown or not specified.
- [CPRerouteReason.waypointModified](./cpreroutereason/waypointmodified.md)
  An existing waypoint was modified or updated.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpreroutereason)*