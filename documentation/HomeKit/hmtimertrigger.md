# HMTimerTrigger

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

A trigger to activate an action set based on a periodic timer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMTimerTrigger
```

```objc
@interface HMTimerTrigger : HMTrigger
```

## Overview

When a timer trigger is enabled using [`enable(_:completionHandler:)`](./hmtrigger/enable%28_,completionhandler%29.md), the system checks to verify that the timer trigger’s fire date, time zone, and recurrence rules yield a next fire date that is in the future.

## Topics

### Creating a timer trigger
- [init(name: String, fireDate: Date, recurrence: DateComponents?)](./hmtimertrigger/init%28name,firedate,recurrence%29.md)
### Choosing the fire date
- [var fireDate: Date](./hmtimertrigger/firedate.md)
  The time at which the trigger will next fire.
- [func updateFireDate(Date, completionHandler: ((any Error)?) -> Void)](./hmtimertrigger/updatefiredate%28_,completionhandler%29.md)
  Updates the next fire date for the trigger.
### Using recurrence
- [var recurrence: DateComponents?](./hmtimertrigger/recurrence.md)
  The interval on which to repeat firing the trigger.
- [func updateRecurrence(DateComponents?, completionHandler: ((any Error)?) -> Void)](./hmtimertrigger/updaterecurrence%28_,completionhandler%29.md)
  Updates the recurrence interval.
### Deprecated symbols
- [init(name: String, fireDate: Date, timeZone: TimeZone?, recurrence: DateComponents?, recurrenceCalendar: Calendar?)](./hmtimertrigger/init%28name,firedate,timezone,recurrence,recurrencecalendar%29.md)
  Initializes a timer trigger with specified timing information.
- [var timeZone: TimeZone?](./hmtimertrigger/timezone.md)
  The timezone in which to evaluate the fire time.
- [func updateTimeZone(TimeZone?, completionHandler: ((any Error)?) -> Void)](./hmtimertrigger/updatetimezone%28_,completionhandler%29.md)
  Updates the trigger’s time zone.
- [var recurrenceCalendar: Calendar?](./hmtimertrigger/recurrencecalendar.md)
  The calendar in which the recurrence value is evaluated.

## Relationships

### Inherits From
- [HMTrigger](./hmtrigger.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Action Sets
- [class HMActionSet](./hmactionset.md)
  A collection of actions that you trigger as a group.
- [class HMEventTrigger](./hmeventtrigger.md)
  A trigger to activate an action set based on a set of events and optional conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger)*