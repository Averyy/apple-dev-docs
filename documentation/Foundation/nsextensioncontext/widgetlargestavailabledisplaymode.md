# widgetLargestAvailableDisplayMode

**Framework**: Foundation  
**Kind**: property

The largest display mode the widget supports.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+

## Declaration

```swift
var widgetLargestAvailableDisplayMode: NCWidgetDisplayMode { get set }
```

#### Discussion

The default value of this property is [`NCWidgetDisplayMode.compact`](https://developer.apple.com/documentation/NotificationCenter/NCWidgetDisplayMode/compact). At any time, you can change the largest display mode your widget supports by changing the value of this property. For example, you can update the property value as more or less content is available to display in your widget.

## See Also

- [func completeRequest(withBroadcast: URL, broadcastConfiguration: RPBroadcastConfiguration, setupInfo: [String : any NSCoding & NSObjectProtocol]?)](nsextensioncontext/completerequest(withbroadcast:broadcastconfiguration:setupinfo:).md)
  Tells the host app to complete the app extension request with the specified broadcast information.
- [var widgetActiveDisplayMode: NCWidgetDisplayMode](nsextensioncontext/widgetactivedisplaymode.md)
  The active display mode of the widget.
- [func widgetMaximumSize(for: NCWidgetDisplayMode) -> CGSize](nsextensioncontext/widgetmaximumsize(for:).md)
  Returns the maximum size for the specified widget display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/widgetlargestavailabledisplaymode)*