# ContentCachingInformationResponse.StatusResponse.AlertsItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an alert from the content cache.

**Availability**:
- macOS 10.15.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ContentCachingInformationResponse.StatusResponse.AlertsItem
```

## Properties

- `cacheLimit` (integer): The limit, in bytes, for the content cache at the time of the alert. This value only applies to `AssetCacheLowSpaceAlert` and `AssetCacheNoSpaceAlert` types.
- `className` (string) *(required)*: The type of the alert.
- `pathPreventingAccess` (string): The subpath of the resource that was missing or inaccessible at the time of the alert. This value only applies to the `AssetCacheResourceMissingAlert` type.
- `postDate` (date) *(required)*: The date of the alert.
- `reservedVolumeSpace` (integer): The space, in bytes, that the system reserves at the time of the alert. This value only applies to the `AssetCacheLowSpaceAlert` and `AssetCacheNoSpaceAlert` types.
- `resource` (string): The resource that was missing or inaccessible at the time of the alert. This value only applies to the `AssetCacheResourceMissingAlert` type.

## See Also

- [object ContentCachingInformationResponse.StatusResponse.AlertsForPeerFilterRanges](contentcachinginformationresponse/statusresponse-data.dictionary/alertsforpeerfilterranges-data.dictionary.md)
  A dictionary that contains alerts for peer filter ranges.
- [object ContentCachingInformationResponse.StatusResponse.CacheDetails](contentcachinginformationresponse/statusresponse-data.dictionary/cachedetails-data.dictionary.md)
  A dictionary that describes disk space the content cache uses.
- [object ContentCachingInformationResponse.StatusResponse.DataMigrationError](contentcachinginformationresponse/statusresponse-data.dictionary/datamigrationerror-data.dictionary.md)
  A dictionary that describes a data migration error.
- [object ContentCachingInformationResponse.StatusResponse.ParentsItem](contentcachinginformationresponse/statusresponse-data.dictionary/parentsitem.md)
  A dictionary that describes a parent content cache.
- [object ContentCachingInformationResponse.StatusResponse.PeersItem](contentcachinginformationresponse/statusresponse-data.dictionary/peersitem.md)
  A dictionary that describes a peer content cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationresponse/statusresponse-data.dictionary/alertsitem)*