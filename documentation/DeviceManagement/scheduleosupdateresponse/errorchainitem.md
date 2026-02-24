# ScheduleOSUpdateResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- tvOS 12.0+

## Declaration

```swift
object ScheduleOSUpdateResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

- [object ScheduleOSUpdateResponse.UpdateResultsItem](scheduleosupdateresponse/updateresultsitem.md)
  The response dictionary that describes the result of processing an operating-system update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdateresponse/errorchainitem)*