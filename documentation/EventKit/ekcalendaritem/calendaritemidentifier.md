# calendarItemIdentifier

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The calendar item’s unique identifier.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var calendarItemIdentifier: String { get }
```

```objc
@property (nonatomic, readonly) NSString * calendarItemIdentifier;
```

## Discussion

This property is set when the calendar item is created and can be used as a local identifier. Use [`calendarItem(withIdentifier:)`](../ekeventstore/calendaritem%28withidentifier%29.md) to look up the item by this value.

A full sync with the calendar will lose this identifier. You should have a plan for dealing with a calendar whose identifier is no longer fetch-able by caching its other properties.

## See Also

### Related Documentation
- [var calendarIdentifier: String](../ekcalendar/calendaridentifier.md)
  A unique identifier for the calendar.
- [Calendar and Reminders Programming Guide](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/EventKitProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009765)
### Accessing Calendar Items
- [var calendarItemExternalIdentifier: String!](./calendaritemexternalidentifier.md)
  The calendar item’s external identifier as provided by the calendar server.
- [var uuid: String](./uuid.md)
  The calendar item’s unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/calendaritemidentifier)*