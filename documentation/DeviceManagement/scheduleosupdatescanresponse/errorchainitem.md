# ScheduleOSUpdateScanResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that describes an error chain item.

**Availability**:
- macOS 10.11+ - Deprecated in 26.0

> **Deprecated**: **Removed** Use the declarative management software update features instead.

## Declaration

```
object ScheduleOSUpdateScanResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)* *(deprecated)*: The error code.
- `ErrorDomain` (string) *(required)* *(deprecated)*: The error domain.
- `LocalizedDescription` (string) *(required)* *(deprecated)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string) *(deprecated)*: A description of the error in U.S. English.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdatescanresponse/errorchainitem)*