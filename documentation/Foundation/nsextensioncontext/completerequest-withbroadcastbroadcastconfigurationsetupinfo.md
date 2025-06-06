# completeRequest(withBroadcast:broadcastConfiguration:setupInfo:)

**Framework**: Foundation  
**Kind**: method

Tells the host app to complete the app extension request with the specified broadcast information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func completeRequest(withBroadcast broadcastURL: URL, broadcastConfiguration: RPBroadcastConfiguration, setupInfo: [String : any NSCoding & NSObjectProtocol]?)
```

## See Also

- [var widgetActiveDisplayMode: NCWidgetDisplayMode](nsextensioncontext/widgetactivedisplaymode.md)
  The active display mode of the widget.
- [var widgetLargestAvailableDisplayMode: NCWidgetDisplayMode](nsextensioncontext/widgetlargestavailabledisplaymode.md)
  The largest display mode the widget supports.
- [func widgetMaximumSize(for: NCWidgetDisplayMode) -> CGSize](nsextensioncontext/widgetmaximumsize(for:).md)
  Returns the maximum size for the specified widget display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/completerequest(withbroadcast:broadcastconfiguration:setupinfo:))*