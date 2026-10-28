# widgetActiveDisplayModeDidChange(_:withMaximumSize:)

**Framework**: Notification Center  
**Kind**: method  
**Role**: Instance Method

Called when the active display mode changes.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0
- iPadOS 10.0+ - Deprecated in 14.0
- Mac Catalyst 10.0+ - Deprecated in 14.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
optional func widgetActiveDisplayModeDidChange(_ activeDisplayMode: NCWidgetDisplayMode, withMaximumSize maxSize: CGSize)
```

```objc
- (void) widgetActiveDisplayModeDidChange:(NCWidgetDisplayMode) activeDisplayMode withMaximumSize:(CGSize) maxSize;
```

## Discussion

You might implement this method if your widget should change its [`preferredContentSize`](../../UIKit/uiviewcontroller/preferredcontentsize.md) value to better accommodate the new display mode.

Widgets displayed as [`NCWidgetDisplayMode.compact`](../ncwidgetdisplaymode/compact.md) have a fixed size passed in the `maxSize` parameter.

## Parameters

- `activeDisplayMode`: The new active display mode. See [`NCWidgetDisplayMode`](../ncwidgetdisplaymode.md) for possible values.
- `maxSize`: A [`CGSize`](../../CoreFoundation/cgsize.md) object that represents the new maximum size this widget can have.

## See Also

### Customizing the Display
- [func widgetMarginInsets(forProposedMarginInsets: UIEdgeInsets) -> UIEdgeInsets](./widgetmargininsets%28forproposedmargininsets%29.md)
  Called to let a widget accept the default margin inset values or return custom values to use instead.
- [enum NCWidgetDisplayMode](../ncwidgetdisplaymode.md)
  The modes that can be toggled between when the user activates the More button for a widget running in iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/widgetactivedisplaymodedidchange(_:withmaximumsize:))*