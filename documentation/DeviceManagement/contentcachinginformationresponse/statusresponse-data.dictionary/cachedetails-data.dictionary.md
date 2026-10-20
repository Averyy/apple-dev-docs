# ContentCachingInformationResponse.StatusResponse.CacheDetails

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that describes disk space the content cache uses.

**Availability**:
- macOS 10.15.4+

## Declaration

```
object ContentCachingInformationResponse.StatusResponse.CacheDetails
```

## Properties

- `Category Name` (integer) *(required)*: The amount of disk space, in bytes, that this category of cached content uses.

## See Also

### Objects
- [object ContentCachingInformationResponse.StatusResponse.AlertsForPeerFilterRanges](./alertsforpeerfilterranges-data.dictionary.md)
  A dictionary that contains alerts for peer filter ranges.
- [object ContentCachingInformationResponse.StatusResponse.AlertsItem](./alertsitem.md)
  A dictionary that describes an alert from the content cache.
- [object ContentCachingInformationResponse.StatusResponse.DataMigrationError](./datamigrationerror-data.dictionary.md)
  A dictionary that describes a data migration error.
- [object ContentCachingInformationResponse.StatusResponse.ParentsItem](./parentsitem.md)
  A dictionary that describes a parent content cache.
- [object ContentCachingInformationResponse.StatusResponse.PeersItem](./peersitem.md)
  A dictionary that describes a peer content cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationresponse/statusresponse-data.dictionary/cachedetails-data.dictionary)*