# ContentCachingInformationResponse.StatusResponse.PeersItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes a peer content cache.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
object ContentCachingInformationResponse.StatusResponse.PeersItem
```

## Topics

### Objects
- [object ContentCachingInformationResponse.StatusResponse.PeersItem.Alert](contentcachinginformationresponse/statusresponse-data.dictionary/peersitem/alert-data.dictionary.md)
  A dictionary that describes a peer content cache alert.
- [object ContentCachingInformationResponse.StatusResponse.PeersItem.Details](contentcachinginformationresponse/statusresponse-data.dictionary/peersitem/details-data.dictionary.md)
  A dictionary that contains additional details about the peer content cache.

## Properties

- `address` (string) *(required)*: The local IP address of the peer content cache.
- `alert` (ContentCachingInformationResponse.StatusResponse.PeersItem.Alert): A dictionary that describes an alert related to the peer content cache.
- `details` (ContentCachingInformationResponse.StatusResponse.PeersItem.Details) *(required)*: A dictionary that contains additional details about the peer content cache.
- `friendly` (boolean) *(required)*: If `true`, the peer content cache is able to respond to requests from the content cache.
- `guid` (string) *(required)*: The unique identifier of the peer content cache.
- `healthy` (boolean) *(required)*: If `true`, the peer content cache is able to respond to requests from the content cache.
- `port` (integer) *(required)*: The IP port number the peer content cache listens to for requests.
- `version` (string) *(required)*: The version number of the peer content cache software.

## See Also

- [object ContentCachingInformationResponse.StatusResponse.AlertsForPeerFilterRanges](contentcachinginformationresponse/statusresponse-data.dictionary/alertsforpeerfilterranges-data.dictionary.md)
  A dictionary that contains alerts for peer filter ranges.
- [object ContentCachingInformationResponse.StatusResponse.AlertsItem](contentcachinginformationresponse/statusresponse-data.dictionary/alertsitem.md)
  A dictionary that describes an alert from the content cache.
- [object ContentCachingInformationResponse.StatusResponse.CacheDetails](contentcachinginformationresponse/statusresponse-data.dictionary/cachedetails-data.dictionary.md)
  A dictionary that describes disk space the content cache uses.
- [object ContentCachingInformationResponse.StatusResponse.DataMigrationError](contentcachinginformationresponse/statusresponse-data.dictionary/datamigrationerror-data.dictionary.md)
  A dictionary that describes a data migration error.
- [object ContentCachingInformationResponse.StatusResponse.ParentsItem](contentcachinginformationresponse/statusresponse-data.dictionary/parentsitem.md)
  A dictionary that describes a parent content cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationresponse/statusresponse-data.dictionary/peersitem)*