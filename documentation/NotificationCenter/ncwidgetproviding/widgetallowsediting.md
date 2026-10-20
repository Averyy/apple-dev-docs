# widgetAllowsEditing

**Framework**: Notification Center  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the widget can be edited by users.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
optional var widgetAllowsEditing: Bool { get }
```

```objc
@property (readonly) BOOL widgetAllowsEditing;
```

#### Discussion

When a widget that supports editing sets this property to [`true`](../../Swift/true.md), it automatically gets a system-provided button in its header area that users choose to begin or end editing. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Supporting Editing
- [func widgetDidBeginEditing()](./widgetdidbeginediting%28%29.md)
  Called when a user chooses the widget’s begin editing button.
- [func widgetDidEndEditing()](./widgetdidendediting%28%29.md)
  Called when a widget’s editing session ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/widgetallowsediting)*