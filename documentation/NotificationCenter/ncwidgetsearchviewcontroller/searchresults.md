# searchResults

**Framework**: Notification Center  
**Kind**: property

An array of search results.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var searchResults: [Any]? { get set }
```

#### Discussion

The [`delegate`](ncwidgetsearchviewcontroller/delegate.md) updates this property with the results of the search. For each object in `searchResults`, the search view controller uses the [`searchResultKeyPath`](ncwidgetsearchviewcontroller/searchresultkeypath.md) property to find the description of the object to display in search view.

When a user chooses an item in the search view’s results list, the search view controller calls [`widgetSearch(_:resultSelected:)`](ncwidgetsearchviewdelegate/widgetsearch(_:resultselected:).md) on its delegate. If the widget presented the search view using `presentViewControllerInWidget:`, this action causes the search view to be dismissed by `dismissViewController:`.

## See Also

- [var searchResultKeyPath: String?](ncwidgetsearchviewcontroller/searchresultkeypath.md)
  A key path for the string property to display for each object in the search results array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller/searchresults)*