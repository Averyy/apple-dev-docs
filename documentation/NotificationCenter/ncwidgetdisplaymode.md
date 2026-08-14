# NCWidgetDisplayMode

**Framework**: Notification Center  
**Kind**: enum

The modes that can be toggled between when the user activates the More button for a widget running in iOS.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+

## Declaration

```swift
enum NCWidgetDisplayMode
```

## Topics

### Constants
- [NCWidgetDisplayMode.compact](ncwidgetdisplaymode/compact.md)
  The current height of the widget is compact.
- [NCWidgetDisplayMode.expanded](ncwidgetdisplaymode/expanded.md)
  The current height of the widget is expanded.
### Initializers
- [init?(rawValue: Int)](ncwidgetdisplaymode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func widgetMarginInsets(forProposedMarginInsets: UIEdgeInsets) -> UIEdgeInsets](ncwidgetproviding/widgetmargininsets(forproposedmargininsets:).md)
  Called to let a widget accept the default margin inset values or return custom values to use instead.
- [func widgetActiveDisplayModeDidChange(NCWidgetDisplayMode, withMaximumSize: CGSize)](ncwidgetproviding/widgetactivedisplaymodedidchange(_:withmaximumsize:).md)
  Called when the active display mode changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetdisplaymode)*