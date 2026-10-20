# ContentCachingInformationResponse.StatusResponse.ParentsItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that describes a parent content cache.

**Availability**:
- macOS 10.15.4+

## Declaration

```
object ContentCachingInformationResponse.StatusResponse.ParentsItem
```

## Topics

### Objects
- [object ContentCachingInformationResponse.StatusResponse.ParentsItem.Alert](./parentsitem/alert-data.dictionary.md)
  A dictionary that describes a parent content cache alert.
- [object ContentCachingInformationResponse.StatusResponse.ParentsItem.Details](./parentsitem/details-data.dictionary.md)
  A dictionary that contains additional details about the parent content cache.

## Properties

- `address` (string) *(required)*: The local IP address of the parent content cache.
- `alert` (ContentCachingInformationResponse.StatusResponse.ParentsItem.Alert): A dictionary that describes an alert related to the parent content cache.
- `details` (ContentCachingInformationResponse.StatusResponse.ParentsItem.Details) *(required)*: A dictionary that contains additional details about the parent content cache.
- `guid` (string) *(required)*: The unique identifier of the parent content cache.
- `healthy` (boolean) *(required)*: If `true,` the parent content cache is able to respond to requests from this content cache.
- `port` (integer) *(required)*: The IP port number the parent content cache listens to for requests.
- `version` (string) *(required)*: The version number of the parent content cache software.

## See Also

### Objects
- [object ContentCachingInformationResponse.StatusResponse.AlertsForPeerFilterRanges](./alertsforpeerfilterranges-data.dictionary.md)
  A dictionary that contains alerts for peer filter ranges.
- [object ContentCachingInformationResponse.StatusResponse.AlertsItem](./alertsitem.md)
  A dictionary that describes an alert from the content cache.
- [object ContentCachingInformationResponse.StatusResponse.CacheDetails](./cachedetails-data.dictionary.md)
  A dictionary that describes disk space the content cache uses.
- [object ContentCachingInformationResponse.StatusResponse.DataMigrationError](./datamigrationerror-data.dictionary.md)
  A dictionary that describes a data migration error.
- [object ContentCachingInformationResponse.StatusResponse.PeersItem](./peersitem.md)
  A dictionary that describes a peer content cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationresponse/statusresponse-data.dictionary/parentsitem)*