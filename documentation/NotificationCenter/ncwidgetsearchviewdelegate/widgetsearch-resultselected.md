# widgetSearch(_:resultSelected:)

**Framework**: Notification Center  
**Kind**: method  
**Required**: Yes

Tells the delegate that a user chose the specified search result.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func widgetSearch(_ controller: NCWidgetSearchViewController, resultSelected object: Any)
```

#### Discussion

When this method returns, the search view controller is dismissed.

## Parameters

- `controller`: The widget’s search view controller.
- `object`: The object in the search view controller’s   array that represents the search result chosen by the user.

## See Also

- [func widgetSearchTermCleared(NCWidgetSearchViewController)](ncwidgetsearchviewdelegate/widgetsearchtermcleared(_:).md)
  Tells the delegate that a user cleared the search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewdelegate/widgetsearch(_:resultselected:))*