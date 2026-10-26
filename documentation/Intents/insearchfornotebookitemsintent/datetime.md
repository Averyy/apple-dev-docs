# dateTime

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The value to use when performing date-based searches.

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
var dateTime: INDateComponentsRange? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INDateComponentsRange * dateTime;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INDateComponentsRange * dateTime;
```

#### Discussion

Use the value in the [`dateSearchType`](./datesearchtype.md) property to determine how to apply the specified date to your search criteria.

## See Also

### Searching by Date
- [var dateSearchType: INDateSearchType](./datesearchtype.md)
  An indicator of how to apply date values to your search.
- [enum INDateSearchType](../indatesearchtype.md)
  Constants indicating the type of date-based search to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintent/datetime)*