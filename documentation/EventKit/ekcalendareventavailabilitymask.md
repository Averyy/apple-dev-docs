# EKCalendarEventAvailabilityMask

**Framework**: EventKit  
**Kind**: struct

A bitmask indicating the event availability settings that the calendar can support.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct EKCalendarEventAvailabilityMask
```

## Topics

### Initializers
- [init(rawValue: UInt)](ekcalendareventavailabilitymask/init(rawvalue:).md)
  Creates a calendar event availability mask with the specified raw value.
### Type Properties
- [static var busy: EKCalendarEventAvailabilityMask](ekcalendareventavailabilitymask/busy.md)
  The calendar supports the busy event availability setting.
- [static var free: EKCalendarEventAvailabilityMask](ekcalendareventavailabilitymask/free.md)
  The calendar supports the free event availability setting.
- [static var tentative: EKCalendarEventAvailabilityMask](ekcalendareventavailabilitymask/tentative.md)
  The calendar supports the tentative event availability setting.
- [static var unavailable: EKCalendarEventAvailabilityMask](ekcalendareventavailabilitymask/unavailable.md)
  The calendar supports the unavailable event availability setting.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [enum EKCalendarType](ekcalendartype.md)
  Possible calendar types.
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

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask)*