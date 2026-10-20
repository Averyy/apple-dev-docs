# completeRequest(withBroadcast:broadcastConfiguration:setupInfo:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells the host app to complete the app extension request with the specified broadcast information.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`completeRequest(withBroadcast:setupInfo:)`](./completerequest%28withbroadcast,setupinfo%29.md) instead.

## Declaration

```swift
func completeRequest(withBroadcast broadcastURL: URL, broadcastConfiguration: RPBroadcastConfiguration, setupInfo: [String : any NSCoding & NSObjectProtocol]?)
```

```objc
- (void) completeRequestWithBroadcastURL:(NSURL *) broadcastURL broadcastConfiguration:(RPBroadcastConfiguration *) broadcastConfiguration setupInfo:(NSDictionary<NSString *,NSObject<NSCoding> *> *) setupInfo;
```

## See Also

### Deprecated
- [var widgetActiveDisplayMode: NCWidgetDisplayMode](./widgetactivedisplaymode.md)
  The active display mode of the widget.
- [var widgetLargestAvailableDisplayMode: NCWidgetDisplayMode](./widgetlargestavailabledisplaymode.md)
  The largest display mode the widget supports.
- [func widgetMaximumSize(for: NCWidgetDisplayMode) -> CGSize](./widgetmaximumsize%28for%29.md)
  Returns the maximum size for the specified widget display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/completerequest(withbroadcast:broadcastconfiguration:setupinfo:))*