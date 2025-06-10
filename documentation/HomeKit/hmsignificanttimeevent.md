# HMSignificantTimeEvent

**Framework**: HomeKit  
**Kind**: class

An event that fires at a time offset from a significant time-based event.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class HMSignificantTimeEvent
```

#### Overview

Use this class to represent an event that fires at a time relative to a significant event, for example “30 minutes before sunset”.

## Topics

### Creating a significant time event
- [init(significantEvent: HMSignificantEvent, offset: DateComponents?)](hmsignificanttimeevent/init(significantevent:offset:).md)
  Creates a new significant time event with the specified significant event and offset.
### Inspecting a significant time event
- [var significantEvent: HMSignificantEvent](hmsignificanttimeevent/significantevent.md)
  The significant time-based event that is used to calculate when the event fires.
- [var offset: DateComponents?](hmsignificanttimeevent/offset.md)
  The offset from the significant event that the event fires at.

## Relationships

### Inherits From
- [HMTimeEvent](hmtimeevent.md)
### Inherited By
- [HMMutableSignificantTimeEvent](hmmutablesignificanttimeevent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct HMSignificantEvent](hmsignificantevent.md)
  An event that represents significant time-based events, including sunrise and sunset.
- [class HMMutableSignificantTimeEvent](hmmutablesignificanttimeevent.md)
  A mutable event that fires at the specified temporal offset to a significant event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmsignificanttimeevent)*