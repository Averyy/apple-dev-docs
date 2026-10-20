# widgetActiveDisplayMode

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The active display mode of the widget.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0
- iPadOS 10.0+ - Deprecated in 14.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
var widgetActiveDisplayMode: NCWidgetDisplayMode { get }
```

```objc
@property (nonatomic, assign, readonly) NCWidgetDisplayMode widgetActiveDisplayMode;
```

## See Also

### Deprecated
- [func completeRequest(withBroadcast: URL, broadcastConfiguration: RPBroadcastConfiguration, setupInfo: [String : any NSCoding & NSObjectProtocol]?)](./completerequest%28withbroadcast,broadcastconfiguration,setupinfo%29.md)
  Tells the host app to complete the app extension request with the specified broadcast information.
- [var widgetLargestAvailableDisplayMode: NCWidgetDisplayMode](./widgetlargestavailabledisplaymode.md)
  The largest display mode the widget supports.
- [func widgetMaximumSize(for: NCWidgetDisplayMode) -> CGSize](./widgetmaximumsize%28for%29.md)
  Returns the maximum size for the specified widget display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/widgetactivedisplaymode)*