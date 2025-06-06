# widgetMarginInsets(forProposedMarginInsets:)

**Framework**: Notification Center  
**Kind**: method

Called to let a widget accept the default margin inset values or return custom values to use instead.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+

## Declaration

```swift
optional func widgetMarginInsets(forProposedMarginInsets defaultMarginInset: NSEdgeInsets) -> NSEdgeInsets
```

#### Return Value

A value of type [`UIEdgeInsets`](https://developer.apple.com/documentation/UIKit/UIEdgeInsets) that contains the custom margin insets a widget is using instead of the default values.

#### Discussion

A widget can implement this method to return custom margin inset values to use instead of the default values specified in `defaultMarginInsets`. (If the widget doesn’t need to use custom values, it should return the unchanged default values in its implementation.) If a widget doesn’t implement this method, it automatically receives the default margin inset values.

## Parameters

- `defaultMarginInsets`: The default margin insets that are available to the widget.

## See Also

- [func widgetActiveDisplayModeDidChange(NCWidgetDisplayMode, withMaximumSize: CGSize)](ncwidgetproviding/widgetactivedisplaymodedidchange(_:withmaximumsize:).md)
  Called when the active display mode changes.
- [enum NCWidgetDisplayMode](ncwidgetdisplaymode.md)
  The modes that can be toggled between when the user activates the More button for a widget running in iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/widgetmargininsets(forproposedmargininsets:))*