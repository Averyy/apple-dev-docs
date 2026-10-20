# CustomerEngagementSession.Event

**Framework**: ProximityReader  
**Kind**: enum  
**Role**: Enumeration

Events that occur during a customer engagement session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
enum Event
```

## Topics

### Enumeration Cases
- [CustomerEngagementSession.Event.closed](./event/closed.md)
  An event indicating that the connection to the peer closed.
- [CustomerEngagementSession.Event.connected](./event/connected.md)
  An event indicating that the peer has connected.
- [CustomerEngagementSession.Event.disconnected](./event/disconnected.md)
  An event indicating that the peer has disconnected.
- [CustomerEngagementSession.Event.ready](./event/ready.md)
  An event indicating that the peer is ready to accept requests.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting events during a session
- [let events: any AsyncSequence<CustomerEngagementSession.Event, Never>](./events.md)
  An asynchronous sequence of events that occur during the engagement session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/event)*