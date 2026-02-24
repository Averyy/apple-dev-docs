# ScheduleOSUpdateResponse.UpdateResultsItem

**Framework**: Device Management  
**Kind**: dictionary

The response dictionary that describes the result of processing an operating-system update.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
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

- `ErrorChain` ([ScheduleOSUpdateResponse.UpdateResultsItem.ErrorChainItem]): A dictionary that describes an error chain.
- `InstallAction` (string) *(required)*: The install action that the device scheduled, which is one of the following values: - `Error`: An error occurred during scheduling.
- `DownloadOnly`: Download the software update without installing it.
- `InstallASAP`: Install a previously downloaded software update.
- `NotifyOnly`: Download the software update and notify the user through the App Store. This value is available in macOS 10.11 and later.
- `InstallLater`: Download the software update and install it at a later time. This value is available in macOS 10.11 and later.
- `InstallForceRestart`: Perform the `Default` action, and then force a restart if the update requires it. This value is available in macOS 11 and later.
- `ProductKey` (string) *(required)*: The product key that represents the update.
- `Status` (string) *(required)*: The status of the update, which is one of the following values: - `Idle`: The update is idle.
- `Downloading`: The software update is downloading.
- `DownloadFailed`: The download failed.
- `DownloadRequiresComputer`: Tether the device to download this update. This value is only available in iOS.
- `DownloadInsufficientSpace`: There isn’t enough space to download the update.
- `DownloadInsufficientPower`: There isn’t enough power to download the update.
- `DownloadInsufficientNetwork`: The network capacity is insufficient to download the update.
- `Installing`: The software update is installing.
- `InstallInsufficientSpace`: There isn’t enough space to install the update.
- `InstallInsufficientPower`: There isn’t enough power to install the update.
- `InstallPhoneCallInProgress`: Installation couldn’t occur because a phone call is in progress.
- `InstallFailed`: Installation failed due to an unspecified reason.

## See Also

- [object ScheduleOSUpdateResponse.ErrorChainItem](scheduleosupdateresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdateresponse/updateresultsitem)*