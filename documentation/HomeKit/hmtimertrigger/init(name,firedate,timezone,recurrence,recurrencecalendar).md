# init(name:fireDate:timeZone:recurrence:recurrenceCalendar:)

**Framework**: HomeKit  
**Kind**: init  
**Role**: Initializer

Initializes a timer trigger with specified timing information.

**Availability**:
- iOS 8.0+ - Deprecated in 16.4
- iPadOS 8.0+ - Deprecated in 16.4
- Mac Catalyst 8.0+ - Deprecated in 16.4
- tvOS 10.0+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 9.4

## Declaration

```swift
init(name: String, fireDate: Date, timeZone: TimeZone?, recurrence: DateComponents?, recurrenceCalendar: Calendar?)
```

```objc
- (instancetype) initWithName:(NSString *) name fireDate:(NSDate *) fireDate timeZone:(NSTimeZone *) timeZone recurrence:(NSDateComponents *) recurrence recurrenceCalendar:(NSCalendar *) recurrenceCalendar;
```

#### Return Value

A newly-initialized timer trigger with the specified values.

#### Discussion

A new timer trigger starts out disabled, and must be enabled using [`enable(_:completionHandler:)`](../hmtrigger/enable%28_,completionhandler%29.md) before use.

## Parameters

- `name`: The name of the timer trigger.
- `fireDate`: The first fire date.
- `timeZone`: The time zone for the first fire date. Pass `nil` to use the default time zone. See [`timeZone`](./timezone.md) for a description of how the time zone is interpreted.
- `recurrence`: The recurrence interval on which to fire the trigger. `nil` indicates a one-time trigger.
- `recurrenceCalendar`: The calendar in which to evaluate the recurrence interval of a timer trigger. May be `nil`, in which case the current calendar [`current`](../../Foundation/nscalendar/current.md) is used.

## See Also

### Deprecated symbols
- [var timeZone: TimeZone?](./timezone.md)
  The timezone in which to evaluate the fire time.
- [func updateTimeZone(TimeZone?, completionHandler: ((any Error)?) -> Void)](./updatetimezone%28_,completionhandler%29.md)
  Updates the trigger’s time zone.
- [var recurrenceCalendar: Calendar?](./recurrencecalendar.md)
  The calendar in which the recurrence value is evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger/init(name:firedate:timezone:recurrence:recurrencecalendar:))*