# widgetSearch(_:resultSelected:)

**Framework**: Notification Center  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that a user chose the specified search result.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
func widgetSearch(_ controller: NCWidgetSearchViewController, resultSelected object: Any)
```

```objc
- (void) widgetSearch:(NCWidgetSearchViewController *) controller resultSelected:(id) object;
```

#### Discussion

When this method returns, the search view controller is dismissed.

## Parameters

- `controller`: The widget’s search view controller.
- `object`: The object in the search view controller’s [`searchResults`](../ncwidgetsearchviewcontroller/searchresults.md) array that represents the search result chosen by the user.

## See Also

### Responding to User Choices
- [func widgetSearchTermCleared(NCWidgetSearchViewController)](./widgetsearchtermcleared%28_%29.md)
  Tells the delegate that a user cleared the search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewdelegate/widgetsearch(_:resultselected:))*