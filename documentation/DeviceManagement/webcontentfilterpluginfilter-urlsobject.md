# WebContentFilterPluginFilter_URLsObject

**Framework**: Device Management  
**Kind**: dictionary

Settings that control the URL filter. If not present, the system doesn’t use URL filtering.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
object WebContentFilterPluginFilter_URLsObject
```

## Topics

### Objects
- [object WebContentFilterPluginFilter_URLs_ParametersObject](webcontentfilterpluginfilter_urls_parametersobject.md)
  A dictionary containing URL filter parameters. Required when `Enabled` is `true`.

## Properties

- `Enabled` (boolean) *(required)*: If `true`, the system filters URL requests.
- `Parameters` (WebContentFilterPluginFilter_URLs_ParametersObject): A dictionary containing URL filter parameters. Required when `Enabled` is `true`.

## See Also

- [object WebContentFilterPluginFilter_BrowsersObject](webcontentfilterpluginfilter_browsersobject.md)
  Settings that control the browser filter. If not present, the system doesn’t use browser filtering.
- [object WebContentFilterPluginFilter_PacketsObject](webcontentfilterpluginfilter_packetsobject.md)
  Settings that control the packet filter. If not present, the system doesn’t use packet filtering.
- [object WebContentFilterPluginFilter_SocketsObject](webcontentfilterpluginfilter_socketsobject.md)
  Settings that control the socket filter. If not present, the system doesn’t use socket filtering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/webcontentfilterpluginfilter_urlsobject)*