# HMCalendarEvent

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HMCalendarEvent : HMTimeEvent
```

## Topics

### Creating a calendar event
- [init(fire: DateComponents)](./hmcalendarevent/init%28fire%29.md)
  Creates a calendar event which fires based on the value of the supplied date components.
### Inspecting the calendar event
- [var fireDateComponents: DateComponents](./hmcalendarevent/firedatecomponents.md)
  The date components that specify when the event is triggered.
### Initializers
- [init(fireDateComponents: DateComponents)](./hmcalendarevent/init%28firedatecomponents%29.md)

## Relationships

### Inherits From
- [HMTimeEvent](./hmtimeevent.md)
### Inherited By
- [HMMutableCalendarEvent](./hmmutablecalendarevent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Dates and times
- [class HMMutableCalendarEvent](./hmmutablecalendarevent.md)
  A mutable event that fires at a specified time.
- [class HMTimeEvent](./hmtimeevent.md)
  An abstract superclass for time-based events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcalendarevent)*