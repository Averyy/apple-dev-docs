# ContentCachingInformationResponse.StatusResponse.DataMigrationError

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that describes a data migration error.

**Availability**:
- macOS 10.15.4+

## Declaration

```
object ContentCachingInformationResponse.StatusResponse.DataMigrationError
```

## Topics

### Objects
- [object ContentCachingInformationResponse.StatusResponse.DataMigrationError.UserInfo](./datamigrationerror-data.dictionary/userinfo-data.dictionary.md)
  A dictionary that contains additional information about a data migration error.

## Properties

- `code` (integer) *(required)*: The error code.
- `domain` (string) *(required)*: The error domain.
- `userInfo` (ContentCachingInformationResponse.StatusResponse.DataMigrationError.UserInfo): A dictionary that contains additional information about the error.

## See Also

### Objects
- [object ContentCachingInformationResponse.StatusResponse.AlertsForPeerFilterRanges](./alertsforpeerfilterranges-data.dictionary.md)
  A dictionary that contains alerts for peer filter ranges.
- [object ContentCachingInformationResponse.StatusResponse.AlertsItem](./alertsitem.md)
  A dictionary that describes an alert from the content cache.
- [object ContentCachingInformationResponse.StatusResponse.CacheDetails](./cachedetails-data.dictionary.md)
  A dictionary that describes disk space the content cache uses.
- [object ContentCachingInformationResponse.StatusResponse.ParentsItem](./parentsitem.md)
  A dictionary that describes a parent content cache.
- [object ContentCachingInformationResponse.StatusResponse.PeersItem](./peersitem.md)
  A dictionary that describes a peer content cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationresponse/statusresponse-data.dictionary/datamigrationerror-data.dictionary)*