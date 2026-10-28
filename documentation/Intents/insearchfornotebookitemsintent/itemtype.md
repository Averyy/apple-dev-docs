# itemType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of items to include in your search.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var itemType: INNotebookItemType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INNotebookItemType itemType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INNotebookItemType itemType;
```

## Discussion

Use this property to determine which items to search. When generating the list of search results, include items only of the specified type.

## See Also

### Searching by Type
- [enum INNotebookItemType](../innotebookitemtype.md)
  Constants indicating the types of items to search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintent/itemtype)*