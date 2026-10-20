# widgetDidBeginEditing()

**Framework**: Notification Center  
**Kind**: method  
**Role**: Instance Method

Called when a user chooses the widget’s begin editing button.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
optional func widgetDidBeginEditing()
```

```objc
- (void) widgetDidBeginEditing;
```

#### Discussion

This method can be called when [`widgetAllowsEditing`](./widgetallowsediting.md) is [`true`](../../Swift/true.md).

## See Also

### Supporting Editing
- [var widgetAllowsEditing: Bool](./widgetallowsediting.md)
  A Boolean value indicating whether the widget can be edited by users.
- [func widgetDidEndEditing()](./widgetdidendediting%28%29.md)
  Called when a widget’s editing session ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/widgetdidbeginediting())*