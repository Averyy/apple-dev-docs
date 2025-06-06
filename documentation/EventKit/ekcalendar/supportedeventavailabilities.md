# supportedEventAvailabilities

**Framework**: EventKit  
**Kind**: property

The event availability settings supported by this calendar, as indicated by a bitmask.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var supportedEventAvailabilities: EKCalendarEventAvailabilityMask { get }
```

#### Discussion

If the calendar doesn’t support event availability settings, this value is [`EKCalendarEventAvailabilityNone`](ekcalendareventavailabilitymask/ekcalendareventavailabilitynone.md).

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
- [var isImmutable: Bool](ekcalendar/isimmutable.md)
  A Boolean value indicating whether the calendar’s properties can be edited or deleted.
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
- [var calendarIdentifier: String](ekcalendar/calendaridentifier.md)
  A unique identifier for the calendar.
- [func DATETIME_COMPONENTS_DO_NOT_USE()](datetime_components_do_not_use().md)
  A deprecated function.
- [func DATE_COMPONENTS_DO_NOT_USE()](date_components_do_not_use().md)
  A deprecated function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendar/supportedeventavailabilities)*