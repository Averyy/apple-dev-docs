# SRMediaEventType

**Framework**: SensorKit  
**Kind**: enum  
**Role**: Enumeration

The types of user interaction with media that the sensor tracks.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
enum SRMediaEventType
```

```c
enum SRMediaEventType : NSInteger;
```

## Topics

### Event types
- [SRMediaEventType.onScreen](./srmediaeventtype/onscreen.md)
  An event that occurs when the media appears on the screen.
- [SRMediaEventType.offScreen](./srmediaeventtype/offscreen.md)
  An event that occurs when the media disappears from the screen.
### Initializers
- [init?(rawValue: Int)](./srmediaeventtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Tracking Media Events
- [var eventType: SRMediaEventType](./srmediaevent/eventtype.md)
  The type of user interaction with the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srmediaeventtype)*