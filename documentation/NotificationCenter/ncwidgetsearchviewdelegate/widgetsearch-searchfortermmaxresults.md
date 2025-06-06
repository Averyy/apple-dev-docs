# widgetSearch(_:searchForTerm:maxResults:)

**Framework**: Notification Center  
**Kind**: method  
**Required**: Yes

Asks the delegate to search using the specified term.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func widgetSearch(_ controller: NCWidgetSearchViewController, searchForTerm searchTerm: String, maxResults max: Int)
```

#### Discussion

The search view controller calls this method as soon as a user begins to type. If there is a maximum number of results the search view controller can display, it specifies this number in `max`. The delegate can use `max` to decide how many search results to return.

The delegate sets the search view controller’s [`searchResults`](ncwidgetsearchviewcontroller/searchresults.md) property to the array of search result objects.

## Parameters

- `controller`: The widget’s search view controller.
- `searchTerm`: The term a user entered into the search field.
- `max`: The maximum number of results the search view controller can display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewdelegate/widgetsearch(_:searchforterm:maxresults:))*