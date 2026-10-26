# locationSearchType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An indicator of how to apply location values to your search.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var locationSearchType: INLocationSearchType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INLocationSearchType locationSearchType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INLocationSearchType locationSearchType;
```

#### Discussion

Use the value in this property to determine how to apply the value in the [`location`](./location.md) property to your search results. When the value of this property is [`INLocationSearchType.unknown`](../inlocationsearchtype/unknown.md), do not consider location as part of your search criteria.

## See Also

### Searching for Tasks by Location
- [var location: CLPlacemark?](./location.md)
  The value to use when searching for location-triggered reminders.
- [enum INLocationSearchType](../inlocationsearchtype.md)
  Constants indicating the type of location-based search to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintent/locationsearchtype)*