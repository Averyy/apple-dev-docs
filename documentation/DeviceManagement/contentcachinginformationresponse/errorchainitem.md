# ContentCachingInformationResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that describes an error chain item.

**Availability**:
- macOS 10.15.4+

## Declaration

```
object ContentCachingInformationResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

### Objects
- [object ContentCachingInformationResponse.StatusResponse](./statusresponse-data.dictionary.md)
  A dictionary that contains the status of content caching on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationresponse/errorchainitem)*