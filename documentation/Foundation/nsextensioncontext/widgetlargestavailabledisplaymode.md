# widgetLargestAvailableDisplayMode

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The largest display mode the widget supports.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0
- iPadOS 10.0+ - Deprecated in 14.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
var widgetLargestAvailableDisplayMode: NCWidgetDisplayMode { get set }
```

```objc
@property (nonatomic, assign) NCWidgetDisplayMode widgetLargestAvailableDisplayMode;
```

## Discussion

The default value of this property is [`NCWidgetDisplayMode.compact`](../../NotificationCenter/ncwidgetdisplaymode/compact.md). At any time, you can change the largest display mode your widget supports by changing the value of this property. For example, you can update the property value as more or less content is available to display in your widget.

## See Also

### Deprecated
- [func completeRequest(withBroadcast: URL, broadcastConfiguration: RPBroadcastConfiguration, setupInfo: [String : any NSCoding & NSObjectProtocol]?)](./completerequest%28withbroadcast,broadcastconfiguration,setupinfo%29.md)
  Tells the host app to complete the app extension request with the specified broadcast information.
- [var widgetActiveDisplayMode: NCWidgetDisplayMode](./widgetactivedisplaymode.md)
  The active display mode of the widget.
- [func widgetMaximumSize(for: NCWidgetDisplayMode) -> CGSize](./widgetmaximumsize%28for%29.md)
  Returns the maximum size for the specified widget display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/widgetlargestavailabledisplaymode)*