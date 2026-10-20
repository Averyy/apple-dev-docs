# ContentCachingInformationResponse.StatusResponse.ParentsItem.Alert

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that describes a parent content cache alert.

**Availability**:
- macOS 10.15.4+

## Declaration

```
object ContentCachingInformationResponse.StatusResponse.ParentsItem.Alert
```

## Properties

- `addresses` ([string]) *(required)*: An array of local IP addresses of parent content caches.
- `className` (string) *(required)*: The type of the alert.

  **Allowed Values**: `AssetCacheParentCycleAlert`, `AssetCacheParentDepthAlert`
- `postDate` (date) *(required)*: The date of the alert.

## See Also

### Objects
- [object ContentCachingInformationResponse.StatusResponse.ParentsItem.Details](./details-data.dictionary.md)
  A dictionary that contains additional details about the parent content cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationresponse/statusresponse-data.dictionary/parentsitem/alert-data.dictionary)*