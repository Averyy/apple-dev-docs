# autoupdatingCurrent

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, strong, readonly) NSCalendar * autoupdatingCurrentCalendar;
```

## Return Value

The current logical calendar for the current user.

## Discussion

Settings you get from this calendar do change as the user’s settings change (contrast with [`current`](./current.md)).

Note that if you cache values based on the calendar or related information those caches will of course not be automatically updated by the updating of the calendar object.

## See Also

### Related Documentation
- [init?(calendarIdentifier: NSCalendar.Identifier)](./init%28calendaridentifier%29.md)
  Initializes a calendar according to a given identifier.
- [var calendarIdentifier: NSCalendar.Identifier](./calendaridentifier.md)
  An identifier for the calendar.
### Getting the User’s Calendar
- [class var current: Calendar](./current.md)
  The user’s current calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/autoupdatingcurrent)*