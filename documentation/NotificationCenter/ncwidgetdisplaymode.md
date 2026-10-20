# NCWidgetDisplayMode

**Framework**: Notification Center  
**Kind**: enum  
**Role**: Enumeration

The modes that can be toggled between when the user activates the More button for a widget running in iOS.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0
- iPadOS 10.0+ - Deprecated in 14.0
- Mac Catalyst 10.0+ - Deprecated in 14.0

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
enum NCWidgetDisplayMode
```

```c
enum NCWidgetDisplayMode : NSInteger;
```

## Topics

### Constants
- [NCWidgetDisplayMode.compact](./ncwidgetdisplaymode/compact.md)
  The current height of the widget is compact.
- [NCWidgetDisplayMode.expanded](./ncwidgetdisplaymode/expanded.md)
  The current height of the widget is expanded.
### Initializers
- [init?(rawValue: Int)](./ncwidgetdisplaymode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Customizing the Display
- [func widgetMarginInsets(forProposedMarginInsets: UIEdgeInsets) -> UIEdgeInsets](./ncwidgetproviding/widgetmargininsets%28forproposedmargininsets%29.md)
  Called to let a widget accept the default margin inset values or return custom values to use instead.
- [func widgetActiveDisplayModeDidChange(NCWidgetDisplayMode, withMaximumSize: CGSize)](./ncwidgetproviding/widgetactivedisplaymodedidchange%28_,withmaximumsize%29.md)
  Called when the active display mode changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetdisplaymode)*