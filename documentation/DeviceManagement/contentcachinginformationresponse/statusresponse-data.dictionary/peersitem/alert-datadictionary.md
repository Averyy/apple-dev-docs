# ContentCachingInformationResponse.StatusResponse.PeersItem.Alert

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes a peer content cache alert.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
object ContentCachingInformationResponse.StatusResponse.PeersItem.Alert
```

## Properties

- `addresses` ([string]): An array of local IP addresses of peer content caches.
- `className` (string) *(required)*: The type of the alert.
- `peerAddress` (string): The local IP address of a peer content cache.
- `postDate` (date) *(required)*: The date of the alert.

## See Also

- [object ContentCachingInformationResponse.StatusResponse.PeersItem.Details](contentcachinginformationresponse/statusresponse-data.dictionary/peersitem/details-data.dictionary.md)
  A dictionary that contains additional details about the peer content cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationresponse/statusresponse-data.dictionary/peersitem/alert-data.dictionary)*