# searchResults

**Framework**: Notification Center  
**Kind**: property  
**Role**: Instance Property

An array of search results.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
var searchResults: [Any]? { get set }
```

```objc
@property (copy, nullable) NSArray<id> * searchResults;
```

## Discussion

The [`delegate`](./delegate.md) updates this property with the results of the search. For each object in `searchResults`, the search view controller uses the [`searchResultKeyPath`](./searchresultkeypath.md) property to find the description of the object to display in search view.

When a user chooses an item in the search view’s results list, the search view controller calls [`widgetSearch(_:resultSelected:)`](../ncwidgetsearchviewdelegate/widgetsearch%28_,resultselected%29.md) on its delegate. If the widget presented the search view using `presentViewControllerInWidget:`, this action causes the search view to be dismissed by `dismissViewController:`.

## See Also

### Displaying Search Results
- [var searchResultKeyPath: String?](./searchresultkeypath.md)
  A key path for the string property to display for each object in the search results array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller/searchresults)*