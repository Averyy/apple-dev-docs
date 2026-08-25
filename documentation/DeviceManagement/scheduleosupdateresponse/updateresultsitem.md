# ScheduleOSUpdateResponse.UpdateResultsItem

**Framework**: Device Management  
**Kind**: dictionary

The response dictionary that describes the result of processing an operating-system update.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 12.0+

## Declaration

```swift
object ScheduleOSUpdateResponse.UpdateResultsItem
```

## Topics

### Objects
- [object ScheduleOSUpdateResponse.UpdateResultsItem.ErrorChainItem](scheduleosupdateresponse/updateresultsitem/errorchainitem.md)
  A dictionary that describes an error chain item.

## Properties

- `ErrorChain` ([ScheduleOSUpdateResponse.UpdateResultsItem.ErrorChainItem]): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `InstallAction` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `ProductKey` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `Status` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+

## See Also

- [object ScheduleOSUpdateResponse.ErrorChainItem](scheduleosupdateresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdateresponse/updateresultsitem)*