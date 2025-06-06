# widgetMaximumSize(for:)

**Framework**: Foundation  
**Kind**: method

Returns the maximum size for the specified widget display mode.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+

## Declaration

```swift
func widgetMaximumSize(for displayMode: NCWidgetDisplayMode) -> CGSize
```

## Parameters

- `displayMode`: The active display mode of the widget. For possible values, see  .

## See Also

- [func completeRequest(withBroadcast: URL, broadcastConfiguration: RPBroadcastConfiguration, setupInfo: [String : any NSCoding & NSObjectProtocol]?)](nsextensioncontext/completerequest(withbroadcast:broadcastconfiguration:setupinfo:).md)
  Tells the host app to complete the app extension request with the specified broadcast information.
- [var widgetActiveDisplayMode: NCWidgetDisplayMode](nsextensioncontext/widgetactivedisplaymode.md)
  The active display mode of the widget.
- [var widgetLargestAvailableDisplayMode: NCWidgetDisplayMode](nsextensioncontext/widgetlargestavailabledisplaymode.md)
  The largest display mode the widget supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/widgetmaximumsize(for:))*