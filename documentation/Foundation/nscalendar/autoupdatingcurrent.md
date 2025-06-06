# autoupdatingCurrent

**Framework**: Foundation  
**Kind**: property

A calendar that tracks changes to user’s preferred calendar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var autoupdatingCurrent: Calendar { get }
```

#### Return Value

The current logical calendar for the current user.

#### Discussion

Settings you get from this calendar do change as the user’s settings change (contrast with [`current`](nscalendar/current.md)).

Note that if you cache values based on the calendar or related information those caches will of course not be automatically updated by the updating of the calendar object.

## See Also

- [init?(calendarIdentifier: NSCalendar.Identifier)](nscalendar/init(calendaridentifier:).md)
  Initializes a calendar according to a given identifier.
- [var calendarIdentifier: NSCalendar.Identifier](nscalendar/calendaridentifier.md)
  An identifier for the calendar.
- [class var current: Calendar](nscalendar/current.md)
  The user’s current calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/autoupdatingcurrent)*