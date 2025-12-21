# searchBackwards

**Framework**: Foundation  
**Kind**: property

Specifies that the operation should travel backwards to find the previous match before the given date.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var searchBackwards: NSCalendar.Options { get }
```

## See Also

- [static var wrapComponents: NSCalendar.Options](nscalendar/options/wrapcomponents.md)
  Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.
- [static var matchStrictly: NSCalendar.Options](nscalendar/options/matchstrictly.md)
  Specifies that the operation should travel as far forward or backward as necessary looking for a match.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/options/searchbackwards)*