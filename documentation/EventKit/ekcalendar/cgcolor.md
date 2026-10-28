# cgColor

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The calendar’s color.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var cgColor: CGColor! { get set }
```

```objc
@property (nonatomic, null_unspecified) CGColorRef CGColor;
```

## Discussion

This property is the equivalent of the [`color`](./color.md) property in macOS.

## See Also

### Accessing Calendar Properties
- [enum EKCalendarType](../ekcalendartype.md)
  Possible calendar types.
- [struct EKCalendarEventAvailabilityMask](../ekcalendareventavailabilitymask.md)
  A bitmask indicating the event availability settings that the calendar can support.
- [var allowsContentModifications: Bool](./allowscontentmodifications.md)
  A Boolean value that indicates whether you can add, edit, and delete items in the calendar.
- [var color: NSColor!](./color.md)
  The calendar’s color.
- [var isImmutable: Bool](./isimmutable.md)
  A Boolean value indicating whether the calendar’s properties can be edited or deleted.
- [var title: String](./title.md)
  The calendar’s title.
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

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendar/cgcolor)*