# location

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The value to use when searching for location-triggered reminders.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
@NSCopying
var location: CLPlacemark? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) CLPlacemark * location;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) CLPlacemark * location;
```

## Discussion

When the [`locationSearchType`](./locationsearchtype.md) property is [`INLocationSearchType.byLocationTrigger`](../inlocationsearchtype/bylocationtrigger.md), search for reminders delivered when the user is near the location specified by this property.

## See Also

### Searching for Tasks by Location
- [var locationSearchType: INLocationSearchType](./locationsearchtype.md)
  An indicator of how to apply location values to your search.
- [enum INLocationSearchType](../inlocationsearchtype.md)
  Constants indicating the type of location-based search to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintent/location)*