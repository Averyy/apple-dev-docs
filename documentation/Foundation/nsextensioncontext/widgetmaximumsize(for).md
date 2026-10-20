# widgetMaximumSize(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the maximum size for the specified widget display mode.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0
- iPadOS 10.0+ - Deprecated in 14.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
func widgetMaximumSize(for displayMode: NCWidgetDisplayMode) -> CGSize
```

```objc
- (CGSize) widgetMaximumSizeForDisplayMode:(NCWidgetDisplayMode) displayMode;
```

## Parameters

- `displayMode`: The active display mode of the widget. For possible values, see [`NCWidgetDisplayMode`](../../NotificationCenter/ncwidgetdisplaymode.md).

## See Also

### Deprecated
- [func completeRequest(withBroadcast: URL, broadcastConfiguration: RPBroadcastConfiguration, setupInfo: [String : any NSCoding & NSObjectProtocol]?)](./completerequest%28withbroadcast,broadcastconfiguration,setupinfo%29.md)
  Tells the host app to complete the app extension request with the specified broadcast information.
- [var widgetActiveDisplayMode: NCWidgetDisplayMode](./widgetactivedisplaymode.md)
  The active display mode of the widget.
- [var widgetLargestAvailableDisplayMode: NCWidgetDisplayMode](./widgetlargestavailabledisplaymode.md)
  The largest display mode the widget supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/widgetmaximumsize(for:))*