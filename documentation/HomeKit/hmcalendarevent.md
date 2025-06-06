# HMCalendarEvent

**Framework**: HomeKit  
**Kind**: class

An event that fires at a specified time.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class HMCalendarEvent
```

## Topics

### Creating a calendar event
- [init(fire: DateComponents)](hmcalendarevent/init(fire:).md)
  Creates a calendar event which fires based on the value of the supplied date components.
### Inspecting the calendar event
- [var fireDateComponents: DateComponents](hmcalendarevent/firedatecomponents.md)
  The date components that specify when the event is triggered.

## Relationships

### Inherits From
- [HMTimeEvent](hmtimeevent.md)
### Inherited By
- [HMMutableCalendarEvent](hmmutablecalendarevent.md)
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

## See Also

- [class HMMutableCalendarEvent](hmmutablecalendarevent.md)
  A mutable event that fires at a specified time.
- [class HMTimeEvent](hmtimeevent.md)
  An abstract superclass for time-based events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcalendarevent)*