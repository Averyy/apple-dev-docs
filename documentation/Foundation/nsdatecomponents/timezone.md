# timeZone

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The time zone used to interpret the date components.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var timeZone: TimeZone? { get set }
```

```objc
@property (copy, nullable) NSTimeZone * timeZone;
```

#### Discussion

See [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

### Setting a Calendar and Time Zone
- [var calendar: Calendar?](./calendar.md)
  The calendar used to interpret the date components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/timezone)*