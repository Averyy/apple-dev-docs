# ContentCachingInformationResponse.StatusResponse.PeersItem.Details.Capabilities

**Framework**: Device Management  
**Kind**: dictionary

The capabilities of the peer content cache.

**Availability**:
- macOS 10.15.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ContentCachingInformationResponse.StatusResponse.PeersItem.Details.Capabilities
```

## Properties

- `im` (boolean): If `true`, the peer content cache is capable of imports and uploads.
- `ns` (boolean): If `true`, the peer content cache is capable of handling namespaces, which is an aspect of personal caching.
- `pc` (boolean): If `true`, the peer content cache is capable of caching personal iCloud content.
- `query-parameters` (boolean): If `true`, the peer content cache is capable of handling query parameters in URLs.
- `sc` (boolean): If `true`, the peer content cache is capable of caching shared non-iCloud content.
- `ur` (boolean): If `true`, the peer content cache is capable of prioritizing imports and uploads.

## See Also

- [object ContentCachingInformationResponse.StatusResponse.PeersItem.Details.Local-network](contentcachinginformationresponse/statusresponse-data.dictionary/peersitem/details-data.dictionary/local-network-data.dictionary.md)
  The network details about the peer cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationresponse/statusresponse-data.dictionary/peersitem/details-data.dictionary/capabilities-data.dictionary)*