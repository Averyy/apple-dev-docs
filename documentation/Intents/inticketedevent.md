# INTicketedEvent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes a ticketed event.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INTicketedEvent
```

```objc
@interface INTicketedEvent : NSObject
```

## Topics

### Creating a Ticket Event
- [init(category: INTicketedEventCategory, name: String, eventDuration: INDateComponentsRange, location: CLPlacemark?)](./inticketedevent/init%28category,name,eventduration,location%29.md)
  Creates a ticketed event object with the specified contents and attributes.
### Getting Ticketed Event Information
- [var category: INTicketedEventCategory](./inticketedevent/category.md)
  The type of ticketed event.
- [enum INTicketedEventCategory](./inticketedeventcategory.md)
  Constants that define the type of ticketed event.
- [var eventDuration: INDateComponentsRange](./inticketedevent/eventduration.md)
  The date and time range that indicates the beginning and end of the event.
- [var location: CLPlacemark?](./inticketedevent/location.md)
  The name and location of the ticketed event.
- [var name: String](./inticketedevent/name.md)
  The name of the event.
### Initializers
- [init?(coder: NSCoder)](./inticketedevent/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Getting the Ticketed Event Reservation Information
- [var event: INTicketedEvent](./inticketedeventreservation/event.md)
  An object containing detailed information about the ticketed event.
- [var reservedSeat: INSeat?](./inticketedeventreservation/reservedseat.md)
  The user’s assigned seat for the ticketed event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inticketedevent)*