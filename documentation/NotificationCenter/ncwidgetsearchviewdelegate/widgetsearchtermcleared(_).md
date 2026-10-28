# widgetSearchTermCleared(_:)

**Framework**: Notification Center  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that a user cleared the search field.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
func widgetSearchTermCleared(_ controller: NCWidgetSearchViewController)
```

```objc
- (void) widgetSearchTermCleared:(NCWidgetSearchViewController *) controller;
```

## Discussion

When the delegate receives this message, it should stop the current search.

## Parameters

- `controller`: The widget’s search view controller.

## See Also

### Responding to User Choices
- [func widgetSearch(NCWidgetSearchViewController, resultSelected: Any)](./widgetsearch%28_,resultselected%29.md)
  Tells the delegate that a user chose the specified search result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewdelegate/widgetsearchtermcleared(_:))*