# HMSignificantEvent

**Framework**: HomeKit  
**Kind**: struct  
**Role**: Structure

An event that represents significant time-based events, including sunrise and sunset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct HMSignificantEvent
```

```c
typedef NSString * HMSignificantEvent;
```

## Topics

### Significant event properties
- [static let sunrise: HMSignificantEvent](./hmsignificantevent/sunrise.md)
  An event that fires at sunrise.
- [static let sunset: HMSignificantEvent](./hmsignificantevent/sunset.md)
  An event that fires at sunset.
### Creating a significant event
- [init(String)](./hmsignificantevent/init%28_%29.md)
- [init(rawValue: String)](./hmsignificantevent/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Significant events
- [class HMSignificantTimeEvent](./hmsignificanttimeevent.md)
  An event that fires at a time offset from a significant time-based event.
- [class HMMutableSignificantTimeEvent](./hmmutablesignificanttimeevent.md)
  A mutable event that fires at the specified temporal offset to a significant event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmsignificantevent)*