# name

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the event.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var name: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * name;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * name;
```

## See Also

### Getting Ticketed Event Information
- [var category: INTicketedEventCategory](./category.md)
  The type of ticketed event.
- [enum INTicketedEventCategory](../inticketedeventcategory.md)
  Constants that define the type of ticketed event.
- [var eventDuration: INDateComponentsRange](./eventduration.md)
  The date and time range that indicates the beginning and end of the event.
- [var location: CLPlacemark?](./location.md)
  The name and location of the ticketed event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inticketedevent/name)*