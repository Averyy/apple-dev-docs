# ContentCachingInformationResponse.StatusResponse.AlertsForPeerFilterRanges.ANY index

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes the alerts for the peer filter ranges. The key name is the index into the `PeerFilterRanges` array in the installed `com.apple.AssetCache.managed` payload.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
object ContentCachingInformationResponse.StatusResponse.AlertsForPeerFilterRanges.ANY index
```

## Properties

- `addresses` ([string]) *(required)*: An array of local IP addresses of peer content caches that rejected requests from the content cache.
- `className` (string) *(required)*: The type of the alert.
- `peerFilterRangeIndex` (integer) *(required)*: The index into the `PeerFilterRanges` in the installed ContentCaching payload.
- `postDate` (date) *(required)*: The date of the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationresponse/statusresponse-data.dictionary/alertsforpeerfilterranges-data.dictionary/any-index-data.dictionary)*