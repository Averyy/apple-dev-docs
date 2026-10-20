# widgetList(_:viewControllerForRow:)

**Framework**: Notification Center  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the delegate for a content view controller for the specified row.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
func widgetList(_ list: NCWidgetListViewController, viewControllerForRow row: Int) -> NSViewController
```

```objc
- (NSViewController *) widgetList:(NCWidgetListViewController *) list viewControllerForRow:(NSUInteger) row;
```

#### Return Value

A custom view controller to manage the content in the specified row.

## Parameters

- `list`: The widget’s list view controller that is requesting this content view controller.
- `row`: The number of the row in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate/widgetlist(_:viewcontrollerforrow:))*