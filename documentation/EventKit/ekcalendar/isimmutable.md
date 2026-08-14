# isImmutable

**Framework**: EventKit  
**Kind**: property

A Boolean value indicating whether the calendar’s properties can be edited or deleted.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isImmutable: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the calendar is immutable; otherwise it is not. Events and reminders can still be added to an immutable calendar.

## See Also

- [enum EKCalendarType](ekcalendartype.md)
  Possible calendar types.
- [struct EKCalendarEventAvailabilityMask](ekcalendareventavailabilitymask.md)
  A bitmask indicating the event availability settings that the calendar can support.
- [var allowsContentModifications: Bool](ekcalendar/allowscontentmodifications.md)
  A Boolean value that indicates whether you can add, edit, and delete items in the calendar.
- [var cgColor: CGColor!](ekcalendar/cgcolor.md)
  The calendar’s color.
- [var color: NSColor!](ekcalendar/color.md)
  The calendar’s color.
- [var title: String](ekcalendar/title.md)
  The calendar’s title.
- [var type: EKCalendarType](ekcalendar/type.md)
  The calendar’s type.
- [var allowedEntityTypes: EKEntityMask](ekcalendar/allowedentitytypes.md)
  The entity types this calendar can contain.
- [var source: EKSource!](ekcalendar/source.md)
  The source object representing the account to which this calendar belongs.
- [var isSubscribed: Bool](ekcalendar/issubscribed.md)
  A Boolean value indicating whether the calendar is a subscribed calendar.
- [var supportedEventAvailabilities: EKCalendarEventAvailabilityMask](ekcalendar/supportedeventavailabilities.md)
  The event availability settings supported by this calendar, as indicated by a bitmask.
- [var calendarIdentifier: String](ekcalendar/calendaridentifier.md)
  A unique identifier for the calendar.
- [func DATETIME_COMPONENTS_DO_NOT_USE()](datetime_components_do_not_use().md)
  A deprecated function.
- [func DATE_COMPONENTS_DO_NOT_USE()](date_components_do_not_use().md)
  A deprecated function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendar/isimmutable)*