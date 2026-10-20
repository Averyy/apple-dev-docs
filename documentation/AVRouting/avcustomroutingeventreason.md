# AVCustomRoutingEventReason

**Framework**: AVRouting  
**Kind**: enum  
**Role**: Enumeration

Values that indicate the reason for a routing event.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
enum AVCustomRoutingEventReason
```

```c
enum AVCustomRoutingEventReason : NSInteger;
```

## Topics

### Reasons
- [AVCustomRoutingEventReason.activate](./avcustomroutingeventreason/activate.md)
  A value that indicates that a user selects a route in the picker.
- [AVCustomRoutingEventReason.deactivate](./avcustomroutingeventreason/deactivate.md)
  A value that indicates that a user deselects a route in the picker.
- [AVCustomRoutingEventReason.reactivate](./avcustomroutingeventreason/reactivate.md)
  A value that indicates to reactivate a route a user authorized previously.
### Initializers
- [init?(rawValue: Int)](./avcustomroutingeventreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting an event
- [var route: AVCustomDeviceRoute](./avcustomroutingevent/route.md)
  A route for the event.
- [class AVCustomDeviceRoute](./avcustomdeviceroute.md)
  An object that represents a custom device route.
- [var reason: AVCustomRoutingEventReason](./avcustomroutingevent/reason.md)
  A reason for an event, such as a user request to activate or deactivate a route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingeventreason)*