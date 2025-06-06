# current

**Framework**: Foundation  
**Kind**: property

The user’s current calendar.

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
class var current: Calendar { get }
```

#### Return Value

The logical calendar for the current user.

#### Discussion

The returned calendar is formed from the settings for the current user’s chosen system locale overlaid with any custom settings the user has specified in System Preferences. Settings you get from this calendar do not change as System Preferences are changed, so that your operations are consistent  (contrast with [`autoupdatingCurrent`](nscalendar/autoupdatingcurrent.md)).

## See Also

- [Date and Time Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i)
- [Data Formatting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)
- [init?(calendarIdentifier: NSCalendar.Identifier)](nscalendar/init(calendaridentifier:).md)
  Initializes a calendar according to a given identifier.
- [var calendarIdentifier: NSCalendar.Identifier](nscalendar/calendaridentifier.md)
  An identifier for the calendar.
- [class var autoupdatingCurrent: Calendar](nscalendar/autoupdatingcurrent.md)
  A calendar that tracks changes to user’s preferred calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/current)*