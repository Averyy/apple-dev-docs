# ContentCachingInformationResponse.StatusResponse.PeersItem.Details.Capabilities

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The capabilities of the peer content cache.

**Availability**:
- macOS 10.15.4+

## Declaration

```
object ContentCachingInformationResponse.StatusResponse.PeersItem.Details.Capabilities
```

## Properties

- `im` (boolean): If `true`, the peer content cache is capable of imports and uploads.

  **Default**: `false`
- `ns` (boolean): If `true`, the peer content cache is capable of handling namespaces, which is an aspect of personal caching.

  **Default**: `false`
- `pc` (boolean): If `true`, the peer content cache is capable of caching personal iCloud content.

  **Default**: `false`
- `query-parameters` (boolean): If `true`, the peer content cache is capable of handling query parameters in URLs.

  **Default**: `false`
- `sc` (boolean): If `true`, the peer content cache is capable of caching shared non-iCloud content.

  **Default**: `false`
- `ur` (boolean): If `true`, the peer content cache is capable of prioritizing imports and uploads.

  **Default**: `false`

## See Also

### Objects
- [object ContentCachingInformationResponse.StatusResponse.PeersItem.Details.Local-network](./local-network-data.dictionary.md)
  The network details about the peer cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationresponse/statusresponse-data.dictionary/peersitem/details-data.dictionary/capabilities-data.dictionary)*