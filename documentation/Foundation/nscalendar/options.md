# NSCalendar.Options

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

The options for arithmetic operations involving calendars.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct Options
```

```c
enum NSCalendarOptions : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)
### Constants
- [static var wrapComponents: NSCalendar.Options](./options/wrapcomponents.md)
  Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.
- [static var matchStrictly: NSCalendar.Options](./options/matchstrictly.md)
  Specifies that the operation should travel as far forward or backward as necessary looking for a match.
- [static var searchBackwards: NSCalendar.Options](./options/searchbackwards.md)
  Specifies that the operation should travel backwards to find the previous match before the given date.
- [static var matchPreviousTimePreservingSmallerUnits: NSCalendar.Options](./options/matchprevioustimepreservingsmallerunits.md)
  Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the *previous* existing value of the missing unit and preserves the lower units’ values.
- [static var matchNextTimePreservingSmallerUnits: NSCalendar.Options](./options/matchnexttimepreservingsmallerunits.md)
  Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the *next* existing value of the missing unit and preserves the lower units’ values.
- [static var matchNextTime: NSCalendar.Options](./options/matchnexttime.md)
  Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the *next* existing value of the missing unit and *does not* preserve the lower units’ values.
- [static var matchFirst: NSCalendar.Options](./options/matchfirst.md)
  Specifies that, if there are two or more matching times, the operation should return the first occurrence.
- [static var matchLast: NSCalendar.Options](./options/matchlast.md)
  Specifies that, if there are two or more matching times, the operation should return the last occurrence.
- [var NSWrapCalendarComponents: Int](../nswrapcalendarcomponents.md)
  Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Scanning Dates
- [func startOfDay(for: Date) -> Date](./startofday%28for%29.md)
  Returns the first moment of a given date as a date instance.
- [func enumerateDates(startingAfter: Date, matching: DateComponents, options: NSCalendar.Options, using: (Date?, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratedates%28startingafter,matching,options,using%29.md)
  Computes the dates that match (or most closely match) a given set of components, and calls the block once for each of them, until the enumeration is stopped.
- [func nextDate(after: Date, matching: DateComponents, options: NSCalendar.Options) -> Date?](./nextdate%28after,matching,options%29.md)
  Returns the next date after a given date matching the given components.
- [func nextDate(after: Date, matchingHour: Int, minute: Int, second: Int, options: NSCalendar.Options) -> Date?](./nextdate%28after,matchinghour,minute,second,options%29.md)
  Returns the next date after a given date that matches the given hour, minute, and second, component values.
- [func nextDate(after: Date, matching: NSCalendar.Unit, value: Int, options: NSCalendar.Options) -> Date?](./nextdate%28after,matching,value,options%29.md)
  Returns the next date after a given date matching the given calendar unit value.
- [NSWrapCalendarComponents](../nswrapcalendarcomponents-api.md)
  A legacy constant used to control overflow in date calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/options)*