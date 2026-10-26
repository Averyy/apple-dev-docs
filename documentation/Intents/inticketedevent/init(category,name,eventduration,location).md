# init(category:name:eventDuration:location:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a ticketed event object with the specified contents and attributes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(category: INTicketedEventCategory, name: String, eventDuration: INDateComponentsRange, location: CLPlacemark?)
```

```objc
- (instancetype) initWithCategory:(INTicketedEventCategory) category name:(NSString *) name eventDuration:(INDateComponentsRange *) eventDuration location:(CLPlacemark *) location;
```

#### Return Value

A new [`INTicketedEvent`](../inticketedevent.md) object or `nil` if one can’t be created.

## Parameters

- `category`: The type of ticketed event.
- `name`: The name of the event.
- `eventDuration`: The date and time range that indicates the beginning and end of the event.
- `location`: The name and location of the venue or place for the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inticketedevent/init(category:name:eventduration:location:))*