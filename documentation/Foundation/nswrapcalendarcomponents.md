# NSWrapCalendarComponents

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0 (renamed: NSCalendar.Options.wrapComponents)
- iPadOS 2.0+ - Deprecated in 8.0 (renamed: NSCalendar.Options.wrapComponents)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: NSCalendar.Options.wrapComponents)
- macOS 10.4+ - Deprecated in 10.10 (renamed: NSCalendar.Options.wrapComponents)
- tvOS 9.0+ - Deprecated in 9.0 (renamed: NSCalendar.Options.wrapComponents)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: NSCalendar.Options.wrapComponents)
- watchOS 2.0+ - Deprecated in 2.0 (renamed: NSCalendar.Options.wrapComponents)

> **Deprecated**: Use [`wrapComponents`](./nscalendar/options/wrapcomponents.md) instead.

## Declaration

```swift
var NSWrapCalendarComponents: Int { get }
```

```c
NSWrapCalendarComponents
```

## See Also

### Constants
- [static var wrapComponents: NSCalendar.Options](./nscalendar/options/wrapcomponents.md)
  Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.
- [static var matchStrictly: NSCalendar.Options](./nscalendar/options/matchstrictly.md)
  Specifies that the operation should travel as far forward or backward as necessary looking for a match.
- [static var searchBackwards: NSCalendar.Options](./nscalendar/options/searchbackwards.md)
  Specifies that the operation should travel backwards to find the previous match before the given date.
- [static var matchPreviousTimePreservingSmallerUnits: NSCalendar.Options](./nscalendar/options/matchprevioustimepreservingsmallerunits.md)
  Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the *previous* existing value of the missing unit and preserves the lower units’ values.
- [static var matchNextTimePreservingSmallerUnits: NSCalendar.Options](./nscalendar/options/matchnexttimepreservingsmallerunits.md)
  Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the *next* existing value of the missing unit and preserves the lower units’ values.
- [static var matchNextTime: NSCalendar.Options](./nscalendar/options/matchnexttime.md)
  Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the *next* existing value of the missing unit and *does not* preserve the lower units’ values.
- [static var matchFirst: NSCalendar.Options](./nscalendar/options/matchfirst.md)
  Specifies that, if there are two or more matching times, the operation should return the first occurrence.
- [static var matchLast: NSCalendar.Options](./nscalendar/options/matchlast.md)
  Specifies that, if there are two or more matching times, the operation should return the last occurrence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nswrapcalendarcomponents)*