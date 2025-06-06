# widgetSearchTermCleared(_:)

**Framework**: Notification Center  
**Kind**: method  
**Required**: Yes

Tells the delegate that a user cleared the search field.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func widgetSearchTermCleared(_ controller: NCWidgetSearchViewController)
```

#### Discussion

When the delegate receives this message, it should stop the current search.

## Parameters

- `controller`: The widget’s search view controller.

## See Also

- [func widgetSearch(NCWidgetSearchViewController, resultSelected: Any)](ncwidgetsearchviewdelegate/widgetsearch(_:resultselected:).md)
  Tells the delegate that a user chose the specified search result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewdelegate/widgetsearchtermcleared(_:))*