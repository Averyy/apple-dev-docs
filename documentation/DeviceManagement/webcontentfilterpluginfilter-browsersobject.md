# WebContentFilterPluginFilter_BrowsersObject

**Framework**: Device Management  
**Kind**: dictionary

Settings that control the browser filter. If not present, the system doesn’t use browser filtering.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object WebContentFilterPluginFilter_BrowsersObject
```

## Properties

- `Enabled` (boolean) *(required)*: If `true`, the system enables filtering WebKit traffic.

## See Also

- [object WebContentFilterPluginFilter_PacketsObject](webcontentfilterpluginfilter_packetsobject.md)
  Settings that control the packet filter. If not present, the system doesn’t use packet filtering.
- [object WebContentFilterPluginFilter_SocketsObject](webcontentfilterpluginfilter_socketsobject.md)
  Settings that control the socket filter. If not present, the system doesn’t use socket filtering.
- [object WebContentFilterPluginFilter_URLsObject](webcontentfilterpluginfilter_urlsobject.md)
  Settings that control the URL filter. If not present, the system doesn’t use URL filtering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/webcontentfilterpluginfilter_browsersobject)*