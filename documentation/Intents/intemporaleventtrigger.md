# INTemporalEventTrigger

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A trigger condition based on a date or time.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class INTemporalEventTrigger
```

```objc
@interface INTemporalEventTrigger : NSObject
```

## Overview

When configuring tasks, you can add an [`INTemporalEventTrigger`](./intemporaleventtrigger.md) object to display a reminder at a specific time. Because you specify the time values using an [`INDateComponentsRange`](./indatecomponentsrange.md) object, the trigger condition can occur at a single time or within a range of time. You can also specify a repeating trigger time by specifying a day without a month or year or by specifying a time value without a specific day.

## Topics

### Initializing an Event Trigger
- [init(dateComponentsRange: INDateComponentsRange)](./intemporaleventtrigger/init%28datecomponentsrange%29.md)
  Initializes the event trigger with the specified date information.
### Getting the Trigger Condition
- [var dateComponentsRange: INDateComponentsRange](./intemporaleventtrigger/datecomponentsrange.md)
  The triggering time range for an event.
### Initializers
- [init?(coder: NSCoder)](./intemporaleventtrigger/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Event Triggers
- [class INSpatialEventTrigger](./inspatialeventtrigger.md)
  A trigger condition based on the user’s arrival or departure from a given location.
- [class INTemporalEventTriggerTypeOptionsResolutionResult](./intemporaleventtriggertypeoptionsresolutionresult.md)
  A resolution result that adds a temporal event trigger.
- [struct INDayOfWeekOptions](./indayofweekoptions.md)
  Days of the week.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intemporaleventtrigger)*