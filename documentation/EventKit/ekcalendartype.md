# EKCalendarType

**Framework**: EventKit  
**Kind**: enum

Possible calendar types.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum EKCalendarType
```

## Topics

### Constants
- [EKCalendarType.local](ekcalendartype/local.md)
  A local calendar.
- [EKCalendarType.calDAV](ekcalendartype/caldav.md)
  A CalDAV or iCloud calendar.
- [EKCalendarType.exchange](ekcalendartype/exchange.md)
  An Exchange calendar.
- [EKCalendarType.subscription](ekcalendartype/subscription.md)
  A locally subscribed calendar.
- [EKCalendarType.birthday](ekcalendartype/birthday.md)
  A birthday calendar.
### Initializers
- [init?(rawValue: Int)](ekcalendartype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [var supportedEventAvailabilities: EKCalendarEventAvailabilityMask](ekcalendar/supportedeventavailabilities.md)
  The event availability settings supported by this calendar, as indicated by a bitmask.
- [var calendarIdentifier: String](ekcalendar/calendaridentifier.md)
  A unique identifier for the calendar.
- [func DATETIME_COMPONENTS_DO_NOT_USE()](datetime_components_do_not_use().md)
  A deprecated function.
- [func DATE_COMPONENTS_DO_NOT_USE()](date_components_do_not_use().md)
  A deprecated function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendartype)*