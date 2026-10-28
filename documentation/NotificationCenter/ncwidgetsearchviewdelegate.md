# NCWidgetSearchViewDelegate

**Framework**: Notification Center  
**Kind**: protocol  
**Role**: Protocol

The interface for enabling user searches in the search view controller of a macOS Today widget.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
protocol NCWidgetSearchViewDelegate : NSObjectProtocol
```

```objc
@protocol NCWidgetSearchViewDelegate <NSObject>
```

## Overview

The `NCWidgetSearchViewDelegate` protocol defines methods that enable user searches in the search view controller of a Today widget. The [`delegate`](./ncwidgetsearchviewcontroller/delegate.md) of an [`NCWidgetSearchViewController`](./ncwidgetsearchviewcontroller.md) must adopt the [`NCWidgetSearchViewDelegate`](./ncwidgetsearchviewdelegate.md) protocol.

The search view controller tells its delegate to perform a search on a user’s input and the delegate returns the results by setting the controller’s [`searchResults`](./ncwidgetsearchviewcontroller/searchresults.md) property. The search view controller also tells its delegate when a user clears the search field or chooses a search result, so that the delegate can prepare for a new search or dismissal.

## Topics

### Searching Your Content
- [func widgetSearch(NCWidgetSearchViewController, searchForTerm: String, maxResults: Int)](./ncwidgetsearchviewdelegate/widgetsearch%28_,searchforterm,maxresults%29.md)
  Asks the delegate to search using the specified term.
### Responding to User Choices
- [func widgetSearch(NCWidgetSearchViewController, resultSelected: Any)](./ncwidgetsearchviewdelegate/widgetsearch%28_,resultselected%29.md)
  Tells the delegate that a user chose the specified search result.
- [func widgetSearchTermCleared(NCWidgetSearchViewController)](./ncwidgetsearchviewdelegate/widgetsearchtermcleared%28_%29.md)
  Tells the delegate that a user cleared the search field.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Search View
- [class NCWidgetSearchViewController](./ncwidgetsearchviewcontroller.md)
  An object that provides a default search view within a macOS Today widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewdelegate)*