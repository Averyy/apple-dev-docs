# WebContentFilterPluginFilter_SocketsObject

**Framework**: Device Management  
**Kind**: dictionary

Settings that control the socket filter. If not present, the system doesn’t use socket filtering.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object WebContentFilterPluginFilter_SocketsObject
```

## Properties

- `Enabled` (boolean) *(required)*: If `true`, enables the filtering of socket traffic.
- `ProviderComposedIdentifier` (string): The data provider identifier. This string identifies the filter data provider when the filter starts running. Required when Enabled is true. In iOS and visionOS, the identifier is a bundle ID, for example, “com.example.app”. In macOS, the identifier is a composed identifier. The format of the composed identifier is “Bundle-ID {Designated-Requirement}”. “Bundle-ID” is the bundle identifier string of the provider. “Designated-Requirement” is the designated requirement string the device uses to match the code signature of the provider. For example, “com.example.app {anchor apple generic}”.

## See Also

- [object WebContentFilterPluginFilter_BrowsersObject](webcontentfilterpluginfilter_browsersobject.md)
  Settings that control the browser filter. If not present, the system doesn’t use browser filtering.
- [object WebContentFilterPluginFilter_PacketsObject](webcontentfilterpluginfilter_packetsobject.md)
  Settings that control the packet filter. If not present, the system doesn’t use packet filtering.
- [object WebContentFilterPluginFilter_URLsObject](webcontentfilterpluginfilter_urlsobject.md)
  Settings that control the URL filter. If not present, the system doesn’t use URL filtering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/webcontentfilterpluginfilter_socketsobject)*