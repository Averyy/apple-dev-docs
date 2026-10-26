# INSpatialEvent

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating when to deliver location-related events.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum INSpatialEvent
```

```c
enum INSpatialEvent : NSInteger;
```

## Topics

### Constants
- [INSpatialEvent.unknown](./inspatialevent/unknown.md)
  A constant indicating an unknown trigger condition.
- [INSpatialEvent.arrive](./inspatialevent/arrive.md)
  A constant indicating to deliver events upon arriving at the specified location.
- [INSpatialEvent.depart](./inspatialevent/depart.md)
  A constant indicating to deliver events upon leaving the specified location.
### Initializers
- [init?(rawValue: Int)](./inspatialevent/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Trigger Condition
- [var placemark: CLPlacemark](./inspatialeventtrigger/placemark.md)
  The location that triggers an event.
- [var event: INSpatialEvent](./inspatialeventtrigger/event.md)
  The conditions which trigger an event for the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspatialevent)*