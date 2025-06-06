# searchDescription

**Framework**: Notification Center  
**Kind**: property

A localized description of the nature of the search.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var searchDescription: String? { get set }
```

#### Discussion

The search description is displayed above the search field. If appropriate, the search display controller can change the description to reflect the current status of the search. The default value of this property is “Search”.

## See Also

- [var searchResultsPlaceholderString: String?](ncwidgetsearchviewcontroller/searchresultsplaceholderstring.md)
  A localized phrase displayed in the results list when no search results are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller/searchdescription)*