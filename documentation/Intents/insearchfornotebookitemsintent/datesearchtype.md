# dateSearchType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An indicator of how to apply date values to your search.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var dateSearchType: INDateSearchType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INDateSearchType dateSearchType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INDateSearchType dateSearchType;
```

#### Discussion

Use the value in this property to determine how to apply the value in the [`dateTime`](./datetime.md) property to your search results. When the value of this property is [`INDateSearchType.unknown`](../indatesearchtype/unknown.md), do not consider location as part of your search criteria.

## See Also

### Searching by Date
- [var dateTime: INDateComponentsRange?](./datetime.md)
  The value to use when performing date-based searches.
- [enum INDateSearchType](../indatesearchtype.md)
  Constants indicating the type of date-based search to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintent/datesearchtype)*