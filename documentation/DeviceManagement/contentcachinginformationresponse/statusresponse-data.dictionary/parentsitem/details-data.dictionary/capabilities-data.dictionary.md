# ContentCachingInformationResponse.StatusResponse.ParentsItem.Details.Capabilities

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that describes the capabilities of the parent content cache.

**Availability**:
- macOS 10.15.4+

## Declaration

```
object ContentCachingInformationResponse.StatusResponse.ParentsItem.Details.Capabilities
```

## Properties

- `im` (boolean): If `true`, the parent content cache is capable of imports and uploads.

  **Default**: `false`
- `ns` (boolean): If `true`, the parent content cache is capable of handling namespaces, which is an aspect of personal caching.

  **Default**: `false`
- `pc` (boolean): If `true`, the parent content cache is capable of caching personal iCloud content.

  **Default**: `false`
- `query-parameters` (boolean): If `true`, the parent content cache is capable of handling query parameters in URLs.

  **Default**: `false`
- `sc` (boolean): If `true`, the parent content cache is capable of caching shared non-iCloud content.

  **Default**: `false`
- `ur` (boolean): If `true`, the parent content cache is capable of prioritizing imports and uploads.

  **Default**: `false`

## See Also

### Objects
- [object ContentCachingInformationResponse.StatusResponse.ParentsItem.Details.Local-network](./local-network-data.dictionary.md)
  A dictionary that describes the parent content cache’s connection to its local network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationresponse/statusresponse-data.dictionary/parentsitem/details-data.dictionary/capabilities-data.dictionary)*