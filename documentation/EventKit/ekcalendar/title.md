# title

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The calendar’s title.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var title: String { get set }
```

```objc
@property (nonatomic, copy) NSString * title;
```

## Mentions

- [Creating events and reminders](../creating-events-and-reminders.md)

## See Also

### Accessing Calendar Properties
- [enum EKCalendarType](../ekcalendartype.md)
  Possible calendar types.
- [struct EKCalendarEventAvailabilityMask](../ekcalendareventavailabilitymask.md)
  A bitmask indicating the event availability settings that the calendar can support.
- [var allowsContentModifications: Bool](./allowscontentmodifications.md)
  A Boolean value that indicates whether you can add, edit, and delete items in the calendar.
- [var cgColor: CGColor!](./cgcolor.md)
  The calendar’s color.
- [var color: NSColor!](./color.md)
  The calendar’s color.
- [var isImmutable: Bool](./isimmutable.md)
  A Boolean value indicating whether the calendar’s properties can be edited or deleted.
- [var type: EKCalendarType](./type.md)
  The calendar’s type.
- [var allowedEntityTypes: EKEntityMask](./allowedentitytypes.md)
  The entity types this calendar can contain.
- [var source: EKSource!](./source.md)
  The source object representing the account to which this calendar belongs.
- [var isSubscribed: Bool](./issubscribed.md)
  A Boolean value indicating whether the calendar is a subscribed calendar.
- [var supportedEventAvailabilities: EKCalendarEventAvailabilityMask](./supportedeventavailabilities.md)
  The event availability settings supported by this calendar, as indicated by a bitmask.
- [var calendarIdentifier: String](./calendaridentifier.md)
  A unique identifier for the calendar.
- [func DATETIME_COMPONENTS_DO_NOT_USE()](../datetime_components_do_not_use%28%29.md)
  A deprecated function.
- [func DATE_COMPONENTS_DO_NOT_USE()](../date_components_do_not_use%28%29.md)
  A deprecated function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendar/title)*