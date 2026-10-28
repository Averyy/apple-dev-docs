# updateTimeZone(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Updates the trigger’s time zone.

**Availability**:
- iOS 8.0+ - Deprecated in 16.4
- iPadOS 8.0+ - Deprecated in 16.4
- Mac Catalyst 8.0+ - Deprecated in 16.4
- tvOS 12.0+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 5.0+ - Deprecated in 9.4

> **Deprecated**: Use [`HMEventTrigger`](../hmeventtrigger.md) with [`HMCalendarEvent`](../hmcalendarevent.md) for triggers based on a time-zone-relative time of day.

## Declaration

```swift
func updateTimeZone(_ timeZone: TimeZone?, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func updateTimeZone(_ timeZone: TimeZone?) async throws
```

```objc
- (void) updateTimeZone:(NSTimeZone *) timeZone completionHandler:(void (^)(NSError *error)) completion;
```

## Discussion

See [`timeZone`](./timezone.md) for a description of how the time zone is interpreted.

## Parameters

- `timeZone`: The new time zone; may be `nil`.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Deprecated symbols
- [init(name: String, fireDate: Date, timeZone: TimeZone?, recurrence: DateComponents?, recurrenceCalendar: Calendar?)](./init%28name,firedate,timezone,recurrence,recurrencecalendar%29.md)
  Initializes a timer trigger with specified timing information.
- [var timeZone: TimeZone?](./timezone.md)
  The timezone in which to evaluate the fire time.
- [var recurrenceCalendar: Calendar?](./recurrencecalendar.md)
  The calendar in which the recurrence value is evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger/updatetimezone(_:completionhandler:))*