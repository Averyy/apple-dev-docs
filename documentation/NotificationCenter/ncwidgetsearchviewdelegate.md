# NCWidgetSearchViewDelegate

**Framework**: Notification Center  
**Kind**: protocol

The interface for enabling user searches in the search view controller of a macOS Today widget.

**Availability**:
- macOS 10.10+

## Declaration

```swift
protocol NCWidgetSearchViewDelegate : NSObjectProtocol
```

#### Overview

The `NCWidgetSearchViewDelegate` protocol defines methods that enable user searches in the search view controller of a Today widget. The [`delegate`](ncwidgetsearchviewcontroller/delegate.md) of an [`NCWidgetSearchViewController`](ncwidgetsearchviewcontroller.md) must adopt the [`NCWidgetSearchViewDelegate`](ncwidgetsearchviewdelegate.md) protocol.

The search view controller tells its delegate to perform a search on a user’s input and the delegate returns the results by setting the controller’s [`searchResults`](ncwidgetsearchviewcontroller/searchresults.md) property. The search view controller also tells its delegate when a user clears the search field or chooses a search result, so that the delegate can prepare for a new search or dismissal.

## Topics

### Searching Your Content
- [func widgetSearch(NCWidgetSearchViewController, searchForTerm: String, maxResults: Int)](ncwidgetsearchviewdelegate/widgetsearch(_:searchforterm:maxresults:).md)
  Asks the delegate to search using the specified term.
### Responding to User Choices
- [func widgetSearch(NCWidgetSearchViewController, resultSelected: Any)](ncwidgetsearchviewdelegate/widgetsearch(_:resultselected:).md)
  Tells the delegate that a user chose the specified search result.
- [func widgetSearchTermCleared(NCWidgetSearchViewController)](ncwidgetsearchviewdelegate/widgetsearchtermcleared(_:).md)
  Tells the delegate that a user cleared the search field.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NCWidgetSearchViewController](ncwidgetsearchviewcontroller.md)
  An object that provides a default search view within a macOS Today widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewdelegate)*