# AVCustomRoutingEventReason

**Framework**: AVRouting  
**Kind**: enum

Values that indicate the reason for a routing event.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
enum AVCustomRoutingEventReason
```

## Topics

### Reasons
- [AVCustomRoutingEventReason.activate](avcustomroutingeventreason/activate.md)
  A value that indicates that a user selects a route in the picker.
- [AVCustomRoutingEventReason.deactivate](avcustomroutingeventreason/deactivate.md)
  A value that indicates that a user deselects a route in the picker.
- [AVCustomRoutingEventReason.reactivate](avcustomroutingeventreason/reactivate.md)
  A value that indicates to reactivate a route a user authorized previously.
### Initializers
- [init?(rawValue: Int)](avcustomroutingeventreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var route: AVCustomDeviceRoute](avcustomroutingevent/route.md)
  A route for the event.
- [class AVCustomDeviceRoute](avcustomdeviceroute.md)
  An object that represents a custom device route.
- [var reason: AVCustomRoutingEventReason](avcustomroutingevent/reason.md)
  A reason for an event, such as a user request to activate or deactivate a route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingeventreason)*