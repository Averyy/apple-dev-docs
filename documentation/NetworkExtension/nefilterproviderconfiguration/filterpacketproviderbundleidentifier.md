# filterPacketProviderBundleIdentifier

**Framework**: Network Extension  
**Kind**: property

The bundle identifier of the filter packet provider system extension.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var filterPacketProviderBundleIdentifier: String? { get set }
```

#### Discussion

If this property is `nil`, then the framework uses the bundle identifier of the [`NEFilterPacketProvider`](nefilterpacketprovider.md) extension in the calling app’s bundle. In this case, make sure the calling app’s bundle contains only one [`NEFilterPacketProvider`](nefilterpacketprovider.md), so there’s no ambiguity about which one to use.

This property only applies to system extensions, since macOS doesn’t support implementing a filter packet provider as an app extension.

## See Also

- [var filterDataProviderBundleIdentifier: String?](nefilterproviderconfiguration/filterdataproviderbundleidentifier.md)
  The bundle identifier of the filter data provider system extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/filterpacketproviderbundleidentifier)*