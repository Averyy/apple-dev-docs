# NSCalendar.Options

**Framework**: Foundation  
**Kind**: struct

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

## Topics

### Initializers
- [init(rawValue: UInt)](nscalendar/options/init(rawvalue:).md)
### Constants
- [static var wrapComponents: NSCalendar.Options](nscalendar/options/wrapcomponents.md)
  Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.
- [static var matchStrictly: NSCalendar.Options](nscalendar/options/matchstrictly.md)
  Specifies that the operation should travel as far forward or backward as necessary looking for a match.
- [static var searchBackwards: NSCalendar.Options](nscalendar/options/searchbackwards.md)
  Specifies that the operation should travel backwards to find the previous match before the given date.
- [static var matchPreviousTimePreservingSmallerUnits: NSCalendar.Options](nscalendar/options/matchprevioustimepreservingsmallerunits.md)
  Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the  existing value of the missing unit and preserves the lower units’ values.
- [static var matchNextTimePreservingSmallerUnits: NSCalendar.Options](nscalendar/options/matchnexttimepreservingsmallerunits.md)
  Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the  existing value of the missing unit and preserves the lower units’ values.
- [static var matchNextTime: NSCalendar.Options](nscalendar/options/matchnexttime.md)
  Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the  existing value of the missing unit and  preserve the lower units’ values.
- [static var matchFirst: NSCalendar.Options](nscalendar/options/matchfirst.md)
  Specifies that, if there are two or more matching times, the operation should return the first occurrence.
- [static var matchLast: NSCalendar.Options](nscalendar/options/matchlast.md)
  Specifies that, if there are two or more matching times, the operation should return the last occurrence.
- [static var wrapComponents: NSCalendar.Options](nscalendar/options/wrapcomponents.md)
  Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.
- [static var matchStrictly: NSCalendar.Options](nscalendar/options/matchstrictly.md)
  Specifies that the operation should travel as far forward or backward as necessary looking for a match.
- [static var searchBackwards: NSCalendar.Options](nscalendar/options/searchbackwards.md)
  Specifies that the operation should travel backwards to find the previous match before the given date.
- [static var matchPreviousTimePreservingSmallerUnits: NSCalendar.Options](nscalendar/options/matchprevioustimepreservingsmallerunits.md)
  Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the  existing value of the missing unit and preserves the lower units’ values.
- [static var matchNextTimePreservingSmallerUnits: NSCalendar.Options](nscalendar/options/matchnexttimepreservingsmallerunits.md)
  Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the  existing value of the missing unit and preserves the lower units’ values.
- [static var matchNextTime: NSCalendar.Options](nscalendar/options/matchnexttime.md)
  Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the  existing value of the missing unit and  preserve the lower units’ values.
- [static var matchFirst: NSCalendar.Options](nscalendar/options/matchfirst.md)
  Specifies that, if there are two or more matching times, the operation should return the first occurrence.
- [static var matchLast: NSCalendar.Options](nscalendar/options/matchlast.md)
  Specifies that, if there are two or more matching times, the operation should return the last occurrence.
- [var NSWrapCalendarComponents: Int](nswrapcalendarcomponents.md)
  Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func startOfDay(for: Date) -> Date](nscalendar/startofday(for:).md)
  Returns the first moment of a given date as a date instance.
- [func enumerateDates(startingAfter: Date, matching: DateComponents, options: NSCalendar.Options, using: (Date?, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](nscalendar/enumeratedates(startingafter:matching:options:using:).md)
  Computes the dates that match (or most closely match) a given set of components, and calls the block once for each of them, until the enumeration is stopped.
- [func nextDate(after: Date, matching: DateComponents, options: NSCalendar.Options) -> Date?](nscalendar/nextdate(after:matching:options:).md)
  Returns the next date after a given date matching the given components.
- [func nextDate(after: Date, matchingHour: Int, minute: Int, second: Int, options: NSCalendar.Options) -> Date?](nscalendar/nextdate(after:matchinghour:minute:second:options:).md)
  Returns the next date after a given date that matches the given hour, minute, and second, component values.
- [func nextDate(after: Date, matching: NSCalendar.Unit, value: Int, options: NSCalendar.Options) -> Date?](nscalendar/nextdate(after:matching:value:options:).md)
  Returns the next date after a given date matching the given calendar unit value.
- [NSWrapCalendarComponents](nswrapcalendarcomponents-api.md)
  A legacy constant used to control overflow in date calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/options)*