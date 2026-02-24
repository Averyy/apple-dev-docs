# ContentCachingInformationResponse.StatusResponse.ParentsItem.Details

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains additional details about the parent content cache.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
object ContentCachingInformationResponse.StatusResponse.ParentsItem.Details
```

## Topics

### Objects
- [object ContentCachingInformationResponse.StatusResponse.ParentsItem.Details.Capabilities](contentcachinginformationresponse/statusresponse-data.dictionary/parentsitem/details-data.dictionary/capabilities-data.dictionary.md)
  A dictionary that describes the capabilities of the parent content cache.
- [object ContentCachingInformationResponse.StatusResponse.ParentsItem.Details.Local-network](contentcachinginformationresponse/statusresponse-data.dictionary/parentsitem/details-data.dictionary/local-network-data.dictionary.md)
  A dictionary that describes the parent content cache’s connection to its local network.

## Properties

- `ac-power` (boolean): If `true`, the parent content cache power source is AC; otherwise, an internal battery provides its power.
- `cache-size` (integer): The maximum amount of disk space, in bytes, available to the parent content cache.
- `capabilities` (ContentCachingInformationResponse.StatusResponse.ParentsItem.Details.Capabilities): A dictionary that describes the capabilities of the parent content cache.
- `is-portable` (boolean): If `true`, the parent content cache computer is portable; for example, a laptop.
- `local-network` (ContentCachingInformationResponse.StatusResponse.ParentsItem.Details.Local-network): A dictionary that describes the parent content cache’s connection to its local network.

## See Also

- [object ContentCachingInformationResponse.StatusResponse.ParentsItem.Alert](contentcachinginformationresponse/statusresponse-data.dictionary/parentsitem/alert-data.dictionary.md)
  A dictionary that describes a parent content cache alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationresponse/statusresponse-data.dictionary/parentsitem/details-data.dictionary)*