# widgetActiveDisplayModeDidChange(_:withMaximumSize:)

**Framework**: Notification Center  
**Kind**: method

Called when the active display mode changes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+

## Declaration

```swift
optional func widgetActiveDisplayModeDidChange(_ activeDisplayMode: NCWidgetDisplayMode, withMaximumSize maxSize: CGSize)
```

#### Discussion

You might implement this method if your widget should change its [`preferredContentSize`](https://developer.apple.com/documentation/UIKit/UIViewController/preferredContentSize) value to better accommodate the new display mode.

Widgets displayed as [`NCWidgetDisplayMode.compact`](ncwidgetdisplaymode/compact.md) have a fixed size passed in the `maxSize` parameter.

## Parameters

- `activeDisplayMode`: The new active display mode. See   for possible values.
- `maxSize`: A   object that represents the new maximum size this widget can have.

## See Also

- [func widgetMarginInsets(forProposedMarginInsets: UIEdgeInsets) -> UIEdgeInsets](ncwidgetproviding/widgetmargininsets(forproposedmargininsets:).md)
  Called to let a widget accept the default margin inset values or return custom values to use instead.
- [enum NCWidgetDisplayMode](ncwidgetdisplaymode.md)
  The modes that can be toggled between when the user activates the More button for a widget running in iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/widgetactivedisplaymodedidchange(_:withmaximumsize:))*