# CustomerEngagementSession.Event

**Framework**: ProximityReader  
**Kind**: enum

Events that occur during a customer engagement session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum Event
```

## Topics

### Enumeration Cases
- [CustomerEngagementSession.Event.closed](customerengagementsession/event/closed.md)
  An event indicating that the connection to the peer closed.
- [CustomerEngagementSession.Event.connected](customerengagementsession/event/connected.md)
  An event indicating that the peer has connected.
- [CustomerEngagementSession.Event.disconnected](customerengagementsession/event/disconnected.md)
  An event indicating that the peer has disconnected.
- [CustomerEngagementSession.Event.ready](customerengagementsession/event/ready.md)
  An event indicating that the peer is ready to accept requests.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let events: any AsyncSequence<CustomerEngagementSession.Event, Never>](customerengagementsession/events.md)
  An asynchronous sequence of events that occur during the engagement session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/event)*