# widgetDidEndEditing()

**Framework**: Notification Center  
**Kind**: method  
**Role**: Instance Method

Called when a widget’s editing session ends.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
optional func widgetDidEndEditing()
```

```objc
- (void) widgetDidEndEditing;
```

## Discussion

This method is called when a user chooses the widget’s end editing button or when editing is deactivated because editing begins in a different widget. This method can be called when [`widgetAllowsEditing`](./widgetallowsediting.md) is [`true`](../../Swift/true.md).

## See Also

### Supporting Editing
- [var widgetAllowsEditing: Bool](./widgetallowsediting.md)
  A Boolean value indicating whether the widget can be edited by users.
- [func widgetDidBeginEditing()](./widgetdidbeginediting%28%29.md)
  Called when a user chooses the widget’s begin editing button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/widgetdidendediting())*