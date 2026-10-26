# INLocationSearchType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the type of location-based search to perform.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INLocationSearchType is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
enum INLocationSearchType
```

```c
enum INLocationSearchType : NSInteger;
```

## Topics

### Constants
- [INLocationSearchType.unknown](./inlocationsearchtype/unknown.md)
  An unknown search type.
- [INLocationSearchType.byLocationTrigger](./inlocationsearchtype/bylocationtrigger.md)
  A search type that requires matching the trigger location of a reminder to the specified location.
### Initializers
- [init?(rawValue: Int)](./inlocationsearchtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Searching for Tasks by Location
- [var location: CLPlacemark?](./insearchfornotebookitemsintent/location.md)
  The value to use when searching for location-triggered reminders.
- [var locationSearchType: INLocationSearchType](./insearchfornotebookitemsintent/locationsearchtype.md)
  An indicator of how to apply location values to your search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlocationsearchtype)*