# date(era:yearForWeekOfYear:weekOfYear:weekday:hour:minute:second:nanosecond:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a new date created with the given components base on a week-of-year value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func date(era eraValue: Int, yearForWeekOfYear yearValue: Int, weekOfYear weekValue: Int, weekday weekdayValue: Int, hour hourValue: Int, minute minuteValue: Int, second secondValue: Int, nanosecond nanosecondValue: Int) -> Date?
```

```objc
- (NSDate *) dateWithEra:(NSInteger) eraValue yearForWeekOfYear:(NSInteger) yearValue weekOfYear:(NSInteger) weekValue weekday:(NSInteger) weekdayValue hour:(NSInteger) hourValue minute:(NSInteger) minuteValue second:(NSInteger) secondValue nanosecond:(NSInteger) nanosecondValue;
```

#### Return Value

A new `NSDate` instance created with the given components based on a week-of-year calculation, or `nil` if the components do not correspond to a valid date.

## Parameters

- `eraValue`: The value for the era component.
- `yearValue`: The value for the year component.
- `weekValue`: The value for the week-of-year component.
- `weekdayValue`: The value to use as the weekday.
- `hourValue`: The value for the hour component.
- `minuteValue`: The value for the minute component.
- `secondValue`: The value for the second component.
- `nanosecondValue`: The value for the nanosecond component.

## See Also

### Calculating Dates
- [func date(from: DateComponents) -> Date?](./date%28from%29.md)
  Returns a date representing the absolute time calculated from given components.
- [func date(byAdding: DateComponents, to: Date, options: NSCalendar.Options) -> Date?](./date%28byadding,to,options%29.md)
  Returns a date representing the absolute time calculated by adding given components to a given date.
- [func date(byAdding: NSCalendar.Unit, value: Int, to: Date, options: NSCalendar.Options) -> Date?](./date%28byadding,value,to,options%29.md)
  Returns a date representing the absolute time calculated by adding the value of a given component to a given date.
- [func date(bySettingHour: Int, minute: Int, second: Int, of: Date, options: NSCalendar.Options) -> Date?](./date%28bysettinghour,minute,second,of,options%29.md)
  Creates a new date calculated with the given time.
- [func date(bySettingUnit: NSCalendar.Unit, value: Int, of: Date, options: NSCalendar.Options) -> Date?](./date%28bysettingunit,value,of,options%29.md)
  Returns a new date representing the date calculated by setting a specific component of a given date to a given value, while trying to keep lower components the same.
- [func date(era: Int, year: Int, month: Int, day: Int, hour: Int, minute: Int, second: Int, nanosecond: Int) -> Date?](./date%28era,year,month,day,hour,minute,second,nanosecond%29.md)
  Returns a date created with the given components.
- [func nextWeekendStart(AutoreleasingUnsafeMutablePointer<NSDate?>?, interval: UnsafeMutablePointer<TimeInterval>?, options: NSCalendar.Options, after: Date) -> Bool](./nextweekendstart%28_,interval,options,after%29.md)
  Returns by reference the starting date and time interval range of the next weekend period after a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/date(era:yearforweekofyear:weekofyear:weekday:hour:minute:second:nanosecond:))*