# ScheduleOSUpdateResponse.UpdateResultsItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The response dictionary that describes the result of processing an operating-system update.

**Availability**:
- iOS 9.0+ - Deprecated in 26.0
- iPadOS 9.0+ - Deprecated in 26.0
- Mac Catalyst 9.0+ - Deprecated in 26.0
- macOS 10.11+ - Deprecated in 26.0
- tvOS 12.0+ - Deprecated in 26.0

> **Deprecated**: **Removed** Use the declarative management software update features instead.

## Declaration

```
object ScheduleOSUpdateResponse.UpdateResultsItem
```

## Topics

### Objects
- [object ScheduleOSUpdateResponse.UpdateResultsItem.ErrorChainItem](./updateresultsitem/errorchainitem.md)
  A dictionary that describes an error chain item.

## Properties

- `ErrorChain` ([ScheduleOSUpdateResponse.UpdateResultsItem.ErrorChainItem]) *(deprecated)*: ~~A dictionary that describes an error chain.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `InstallAction` (string) *(required)* *(deprecated)*: ~~The install action that the device scheduled, which is one of the following values:~~

  ~~- `Error`: An error occurred during scheduling.~~ ~~- `DownloadOnly`: Download the software update without installing it.~~ ~~- `InstallASAP`: Install a previously downloaded software update.~~ ~~- `NotifyOnly`: Download the software update and notify the user through the App Store. This value is available in macOS 10.11 and later.~~ ~~- `InstallLater`: Download the software update and install it at a later time. This value is available in macOS 10.11 and later.~~ ~~- `InstallForceRestart`: Perform the `Default` action, and then force a restart if the update requires it. This value is available in macOS 11 and later.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+

  **Allowed Values**: `Error`, `DownloadOnly`, `InstallASAP`, `NotifyOnly`, `InstallLater`, `InstallForceRestart`
- `ProductKey` (string) *(required)* *(deprecated)*: ~~The product key that represents the update.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `Status` (string) *(required)* *(deprecated)*: ~~The status of the update, which is one of the following values:~~

  ~~- `Idle`: The update is idle.~~ ~~- `Downloading`: The software update is downloading.~~ ~~- `DownloadFailed`: The download failed.~~ ~~- `DownloadRequiresComputer`: Tether the device to download this update. This value is only available in iOS.~~ ~~- `DownloadInsufficientSpace`: There isn’t enough space to download the update.~~ ~~- `DownloadInsufficientPower`: There isn’t enough power to download the update.~~ ~~- `DownloadInsufficientNetwork`: The network capacity is insufficient to download the update.~~ ~~- `Installing`: The software update is installing.~~ ~~- `InstallInsufficientSpace`: There isn’t enough space to install the update.~~ ~~- `InstallInsufficientPower`: There isn’t enough power to install the update.~~ ~~- `InstallPhoneCallInProgress`: Installation couldn’t occur because a phone call is in progress.~~ ~~- `InstallFailed`: Installation failed due to an unspecified reason.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+

  **Allowed Values**: `Idle`, `Downloading`, `DownloadFailed`, `DownloadRequiresComputer`, `DownloadInsufficientSpace`, `DownloadInsufficientPower`, `DownloadInsufficientNetwork`, `Installing`, `InstallInsufficientSpace`, `InstallInsufficientPower`, `InstallPhoneCallInProgress`, `InstallFailed`

## See Also

### Objects
- [object ScheduleOSUpdateResponse.ErrorChainItem](./errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdateresponse/updateresultsitem)*