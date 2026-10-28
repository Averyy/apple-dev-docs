# widgetController()

**Framework**: Notification Center  
**Kind**: method  
**Role**: Type Method

Returns a widget controller used to specify whether a widget has content to display.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
class func widgetController() -> Self
```

```objc
+ (instancetype) widgetController;
```

## Return Value

A widget controller.

## Discussion

Both a widget and its containing app can get a widget controller object to specify whether there is content the widget should display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller/widgetcontroller())*