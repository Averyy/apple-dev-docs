# INTicketedEventCategory

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that define the type of ticketed event.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INTicketedEventCategory
```

```c
enum INTicketedEventCategory : NSInteger;
```

## Topics

### Constants
- [INTicketedEventCategory.unknown](./inticketedeventcategory/unknown.md)
  The ticketed event category is unknown.
- [INTicketedEventCategory.movie](./inticketedeventcategory/movie.md)
  The ticketed event is a movie.
### Initializers
- [init?(rawValue: Int)](./inticketedeventcategory/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting Ticketed Event Information
- [var category: INTicketedEventCategory](./inticketedevent/category.md)
  The type of ticketed event.
- [var eventDuration: INDateComponentsRange](./inticketedevent/eventduration.md)
  The date and time range that indicates the beginning and end of the event.
- [var location: CLPlacemark?](./inticketedevent/location.md)
  The name and location of the ticketed event.
- [var name: String](./inticketedevent/name.md)
  The name of the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inticketedeventcategory)*