# OSUpdateStatusResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that describes an error chain item.

**Availability**:
- iOS 9.0+ - Deprecated in 26.0
- iPadOS 9.0+ - Deprecated in 26.0
- Mac Catalyst 9.0+ - Deprecated in 26.0
- macOS 10.11.5+ - Deprecated in 26.0
- tvOS 12.0+ - Deprecated in 26.0

> **Deprecated**: **Removed** Use the declarative management software update features instead.

## Declaration

```
object OSUpdateStatusResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)* *(deprecated)*: The error code.
- `ErrorDomain` (string) *(required)* *(deprecated)*: The error domain.
- `LocalizedDescription` (string) *(required)* *(deprecated)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string) *(deprecated)*: A description of the error in U.S. English.

## See Also

### Objects
- [object OSUpdateStatusResponse.OSUpdateStatusItem](./osupdatestatusitem.md)
  A dictionary that describes the status of a software update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/osupdatestatusresponse/errorchainitem)*