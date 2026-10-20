# searchDescription

**Framework**: Notification Center  
**Kind**: property  
**Role**: Instance Property

A localized description of the nature of the search.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
var searchDescription: String? { get set }
```

```objc
@property (copy, nullable) NSString * searchDescription;
```

#### Discussion

The search description is displayed above the search field. If appropriate, the search display controller can change the description to reflect the current status of the search. The default value of this property is “Search”.

## See Also

### Displaying the Search Interface
- [var searchResultsPlaceholderString: String?](./searchresultsplaceholderstring.md)
  A localized phrase displayed in the results list when no search results are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller/searchdescription)*