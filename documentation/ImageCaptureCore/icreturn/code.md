# ICReturn.Code

**Framework**: ImageCaptureCore  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
enum Code
```

```c
enum ICReturnCode : NSInteger;
```

## Topics

### Enumeration Cases
- [ICReturn.Code.communicationTimedOut](./code/communicationtimedout.md)
- [ICReturn.Code.deleteFilesCanceled](./code/deletefilescanceled.md)
- [ICReturn.Code.deleteFilesFailed](./code/deletefilesfailed.md)
- [ICReturn.Code.deviceCouldNotPair](./code/devicecouldnotpair.md)
- [ICReturn.Code.deviceCouldNotUnpair](./code/devicecouldnotunpair.md)
- [ICReturn.Code.deviceFailedToCloseSession](./code/devicefailedtoclosesession.md)
- [ICReturn.Code.deviceFailedToOpenSession](./code/devicefailedtoopensession.md)
- [ICReturn.Code.deviceFailedToTakePicture](./code/devicefailedtotakepicture.md)
- [ICReturn.Code.deviceIsPasscodeLocked](./code/deviceispasscodelocked.md)
- [ICReturn.Code.deviceNeedsCredentials](./code/deviceneedscredentials.md)
- [ICReturn.Code.deviceSoftwareInstallationCanceled](./code/devicesoftwareinstallationcanceled.md)
- [ICReturn.Code.deviceSoftwareInstallationCompleted](./code/devicesoftwareinstallationcompleted.md)
- [ICReturn.Code.deviceSoftwareInstallationFailed](./code/devicesoftwareinstallationfailed.md)
- [ICReturn.Code.deviceSoftwareIsBeingInstalled](./code/devicesoftwareisbeinginstalled.md)
- [ICReturn.Code.deviceSoftwareNotAvailable](./code/devicesoftwarenotavailable.md)
- [ICReturn.Code.deviceSoftwareNotInstalled](./code/devicesoftwarenotinstalled.md)
- [ICReturn.Code.downloadCanceled](./code/downloadcanceled.md)
- [ICReturn.Code.downloadFailed](./code/downloadfailed.md)
- [ICReturn.Code.failedToCompletePassThroughCommand](./code/failedtocompletepassthroughcommand.md)
- [ICReturn.Code.failedToCompleteSendMessageRequest](./code/failedtocompletesendmessagerequest.md)
- [ICReturn.Code.failedToDisabeTethering](./code/failedtodisabetethering.md)
- [ICReturn.Code.failedToEnabeTethering](./code/failedtoenabetethering.md)
- [ICReturn.Code.invalidParam](./code/invalidparam.md)
- [ICReturn.Code.receivedUnsolicitedScannerErrorInfo](./code/receivedunsolicitedscannererrorinfo.md)
- [ICReturn.Code.receivedUnsolicitedScannerStatusInfo](./code/receivedunsolicitedscannerstatusinfo.md)
- [ICReturn.Code.scanOperationCanceled](./code/scanoperationcanceled.md)
- [ICReturn.Code.scannerFailedToCompleteOverviewScan](./code/scannerfailedtocompleteoverviewscan.md)
- [ICReturn.Code.scannerFailedToCompleteScan](./code/scannerfailedtocompletescan.md)
- [ICReturn.Code.scannerFailedToSelectFunctionalUnit](./code/scannerfailedtoselectfunctionalunit.md)
- [ICReturn.Code.scannerInUseByLocalUser](./code/scannerinusebylocaluser.md)
- [ICReturn.Code.scannerInUseByRemoteUser](./code/scannerinusebyremoteuser.md)
- [ICReturn.Code.success](./code/success.md)
- [ICReturn.Code.uploadFailed](./code/uploadfailed.md)
- [ICReturn.Code.deviceIsBusyEnumerating](./code/deviceisbusyenumerating.md)
- [ICReturn.Code.deviceCommandGeneralFailure](./code/devicecommandgeneralfailure.md)
- [ICReturn.Code.deviceFailedToCompleteTransfer](./code/devicefailedtocompletetransfer.md)
  Failed to complete a data transaction.
- [ICReturn.Code.deviceFailedToSendData](./code/devicefailedtosenddata.md)
  Failed to send data.
- [ICReturn.Code.exFATVolumeInvalid](./code/exfatvolumeinvalid.md)
  EXFAT volume is invalid, and cannot be enumerated.
- [ICReturn.Code.multiErrorDictionary](./code/multierrordictionary.md)
  Multierror
- [ICReturn.Code.sessionNotOpened](./code/sessionnotopened.md)
  Session is not open.
- [ICReturn.Code.communicationTimedOut](./code/communicationtimedout.md)
- [ICReturn.Code.deleteFilesCanceled](./code/deletefilescanceled.md)
- [ICReturn.Code.deleteFilesFailed](./code/deletefilesfailed.md)
- [ICReturn.Code.deviceCouldNotPair](./code/devicecouldnotpair.md)
- [ICReturn.Code.deviceCouldNotUnpair](./code/devicecouldnotunpair.md)
- [ICReturn.Code.deviceFailedToCloseSession](./code/devicefailedtoclosesession.md)
- [ICReturn.Code.deviceFailedToOpenSession](./code/devicefailedtoopensession.md)
- [ICReturn.Code.deviceFailedToTakePicture](./code/devicefailedtotakepicture.md)
- [ICReturn.Code.deviceIsPasscodeLocked](./code/deviceispasscodelocked.md)
- [ICReturn.Code.deviceNeedsCredentials](./code/deviceneedscredentials.md)
- [ICReturn.Code.deviceSoftwareInstallationCanceled](./code/devicesoftwareinstallationcanceled.md)
- [ICReturn.Code.deviceSoftwareInstallationCompleted](./code/devicesoftwareinstallationcompleted.md)
- [ICReturn.Code.deviceSoftwareInstallationFailed](./code/devicesoftwareinstallationfailed.md)
- [ICReturn.Code.deviceSoftwareIsBeingInstalled](./code/devicesoftwareisbeinginstalled.md)
- [ICReturn.Code.deviceSoftwareNotAvailable](./code/devicesoftwarenotavailable.md)
- [ICReturn.Code.deviceSoftwareNotInstalled](./code/devicesoftwarenotinstalled.md)
- [ICReturn.Code.downloadCanceled](./code/downloadcanceled.md)
- [ICReturn.Code.downloadFailed](./code/downloadfailed.md)
- [ICReturn.Code.failedToCompletePassThroughCommand](./code/failedtocompletepassthroughcommand.md)
- [ICReturn.Code.failedToCompleteSendMessageRequest](./code/failedtocompletesendmessagerequest.md)
- [ICReturn.Code.failedToDisabeTethering](./code/failedtodisabetethering.md)
- [ICReturn.Code.failedToEnabeTethering](./code/failedtoenabetethering.md)
- [ICReturn.Code.invalidParam](./code/invalidparam.md)
- [ICReturn.Code.receivedUnsolicitedScannerErrorInfo](./code/receivedunsolicitedscannererrorinfo.md)
- [ICReturn.Code.receivedUnsolicitedScannerStatusInfo](./code/receivedunsolicitedscannerstatusinfo.md)
- [ICReturn.Code.scanOperationCanceled](./code/scanoperationcanceled.md)
- [ICReturn.Code.scannerFailedToCompleteOverviewScan](./code/scannerfailedtocompleteoverviewscan.md)
- [ICReturn.Code.scannerFailedToCompleteScan](./code/scannerfailedtocompletescan.md)
- [ICReturn.Code.scannerFailedToSelectFunctionalUnit](./code/scannerfailedtoselectfunctionalunit.md)
- [ICReturn.Code.scannerInUseByLocalUser](./code/scannerinusebylocaluser.md)
- [ICReturn.Code.scannerInUseByRemoteUser](./code/scannerinusebyremoteuser.md)
- [ICReturn.Code.success](./code/success.md)
- [ICReturn.Code.uploadFailed](./code/uploadfailed.md)
- [ICReturn.Code.deviceIsBusyEnumerating](./code/deviceisbusyenumerating.md)
- [ICReturn.Code.deviceCommandGeneralFailure](./code/devicecommandgeneralfailure.md)
- [ICReturn.Code.deviceFailedToCompleteTransfer](./code/devicefailedtocompletetransfer.md)
  Failed to complete a data transaction.
- [ICReturn.Code.deviceFailedToSendData](./code/devicefailedtosenddata.md)
  Failed to send data.
- [ICReturn.Code.exFATVolumeInvalid](./code/exfatvolumeinvalid.md)
  EXFAT volume is invalid, and cannot be enumerated.
- [ICReturn.Code.multiErrorDictionary](./code/multierrordictionary.md)
  Multierror
- [ICReturn.Code.sessionNotOpened](./code/sessionnotopened.md)
  Session is not open.
### Constants
- [ICReturn.Code.communicationTimedOut](./code/communicationtimedout.md)
- [ICReturn.Code.deleteFilesCanceled](./code/deletefilescanceled.md)
- [ICReturn.Code.deleteFilesFailed](./code/deletefilesfailed.md)
- [ICReturn.Code.deviceCouldNotPair](./code/devicecouldnotpair.md)
- [ICReturn.Code.deviceCouldNotUnpair](./code/devicecouldnotunpair.md)
- [ICReturn.Code.deviceFailedToCloseSession](./code/devicefailedtoclosesession.md)
- [ICReturn.Code.deviceFailedToOpenSession](./code/devicefailedtoopensession.md)
- [ICReturn.Code.deviceFailedToTakePicture](./code/devicefailedtotakepicture.md)
- [ICReturn.Code.deviceIsPasscodeLocked](./code/deviceispasscodelocked.md)
- [ICReturn.Code.deviceNeedsCredentials](./code/deviceneedscredentials.md)
- [ICReturn.Code.deviceSoftwareInstallationCanceled](./code/devicesoftwareinstallationcanceled.md)
- [ICReturn.Code.deviceSoftwareInstallationCompleted](./code/devicesoftwareinstallationcompleted.md)
- [ICReturn.Code.deviceSoftwareInstallationFailed](./code/devicesoftwareinstallationfailed.md)
- [ICReturn.Code.deviceSoftwareIsBeingInstalled](./code/devicesoftwareisbeinginstalled.md)
- [ICReturn.Code.deviceSoftwareNotAvailable](./code/devicesoftwarenotavailable.md)
- [ICReturn.Code.deviceSoftwareNotInstalled](./code/devicesoftwarenotinstalled.md)
- [ICReturn.Code.downloadCanceled](./code/downloadcanceled.md)
- [ICReturn.Code.downloadFailed](./code/downloadfailed.md)
- [ICReturn.Code.failedToCompletePassThroughCommand](./code/failedtocompletepassthroughcommand.md)
- [ICReturn.Code.failedToCompleteSendMessageRequest](./code/failedtocompletesendmessagerequest.md)
- [ICReturn.Code.failedToDisabeTethering](./code/failedtodisabetethering.md)
- [ICReturn.Code.failedToEnabeTethering](./code/failedtoenabetethering.md)
- [ICReturn.Code.invalidParam](./code/invalidparam.md)
- [ICReturn.Code.receivedUnsolicitedScannerErrorInfo](./code/receivedunsolicitedscannererrorinfo.md)
- [ICReturn.Code.receivedUnsolicitedScannerStatusInfo](./code/receivedunsolicitedscannerstatusinfo.md)
- [ICReturn.Code.scanOperationCanceled](./code/scanoperationcanceled.md)
- [ICReturn.Code.scannerFailedToCompleteOverviewScan](./code/scannerfailedtocompleteoverviewscan.md)
- [ICReturn.Code.scannerFailedToCompleteScan](./code/scannerfailedtocompletescan.md)
- [ICReturn.Code.scannerFailedToSelectFunctionalUnit](./code/scannerfailedtoselectfunctionalunit.md)
- [ICReturn.Code.scannerInUseByLocalUser](./code/scannerinusebylocaluser.md)
- [ICReturn.Code.scannerInUseByRemoteUser](./code/scannerinusebyremoteuser.md)
- [ICReturn.Code.success](./code/success.md)
- [ICReturn.Code.uploadFailed](./code/uploadfailed.md)
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [ICLegacyReturnCode](../iclegacyreturn/code.md)
- [ICMediaPresentation](../icmediapresentation.md)
- [ICReturnCodeOffset](../icreturncodeoffset.md)
- [ICReturnConnectionErrorCode](../icreturnconnectionerror/code.md)
- [ICReturnDownloadErrorCode](../icreturndownloaderror/code.md)
- [ICReturnMetadataErrorCode](../icreturnmetadataerror/code.md)
- [ICReturnObjectErrorCode](../icreturnobjecterror/code.md)
- [ICReturnPTPDeviceErrorCode](../icreturnptpdeviceerror/code.md)
- [ICReturnThumbnailErrorCode](../icreturnthumbnailerror/code.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icreturn/code)*