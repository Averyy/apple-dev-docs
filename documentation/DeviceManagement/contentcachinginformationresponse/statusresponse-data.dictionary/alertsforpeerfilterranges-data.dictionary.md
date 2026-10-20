# ContentCachingInformationResponse.StatusResponse.AlertsForPeerFilterRanges

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that contains alerts for peer filter ranges.

**Availability**:
- macOS 10.15.4+

## Declaration

```
object ContentCachingInformationResponse.StatusResponse.AlertsForPeerFilterRanges
```

## Topics

### Objects
- [object ContentCachingInformationResponse.StatusResponse.AlertsForPeerFilterRanges.ANY index](./alertsforpeerfilterranges-data.dictionary/any-index-data.dictionary.md)
  A dictionary that describes the alerts for the peer filter ranges. The key name is the index into the `PeerFilterRanges` array in the installed `com.apple.AssetCache.managed` payload.

## Properties

- `ANY index` (ContentCachingInformationResponse.StatusResponse.AlertsForPeerFilterRanges.ANY index) *(required)*: A dictionary that describes the alerts for the peer filter ranges. The key name is the index into the `PeerFilterRanges` array in the installed `com.apple.AssetCache.managed` payload.

## See Also

### Objects
- [object ContentCachingInformationResponse.StatusResponse.AlertsItem](./alertsitem.md)
  A dictionary that describes an alert from the content cache.
- [object ContentCachingInformationResponse.StatusResponse.CacheDetails](./cachedetails-data.dictionary.md)
  A dictionary that describes disk space the content cache uses.
- [object ContentCachingInformationResponse.StatusResponse.DataMigrationError](./datamigrationerror-data.dictionary.md)
  A dictionary that describes a data migration error.
- [object ContentCachingInformationResponse.StatusResponse.ParentsItem](./parentsitem.md)
  A dictionary that describes a parent content cache.
- [object ContentCachingInformationResponse.StatusResponse.PeersItem](./peersitem.md)
  A dictionary that describes a peer content cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationresponse/statusresponse-data.dictionary/alertsforpeerfilterranges-data.dictionary)*