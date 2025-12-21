# ICReturn

**Framework**: ImageCaptureCore  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
struct ICReturn
```

## Topics

### Type Properties
- [static var communicationTimedOut: ICReturn.Code](icreturn/communicationtimedout.md)
  Communication between different components of Image Capture timed out.
- [static var deleteFilesCanceled: ICReturn.Code](icreturn/deletefilescanceled.md)
  A request to delete files was canceled.
- [static var deleteFilesFailed: ICReturn.Code](icreturn/deletefilesfailed.md)
  A request to delete files failed.
- [static var deviceCommandGeneralFailure: ICReturn.Code](icreturn/devicecommandgeneralfailure.md)
  The device has experienced a general failure.
- [static var deviceCouldNotPair: ICReturn.Code](icreturn/devicecouldnotpair.md)
  A pairing request for an Apple Device failed.
- [static var deviceCouldNotUnpair: ICReturn.Code](icreturn/devicecouldnotunpair.md)
  An unpairing request for an Apple Device failed.
- [static var deviceFailedToCloseSession: ICReturn.Code](icreturn/devicefailedtoclosesession.md)
  Failed to close a session on a specified device.
- [static var deviceFailedToCompleteTransfer: ICReturn.Code](icreturn/devicefailedtocompletetransfer.md)
  Failed to complete a data transaction.
- [static var deviceFailedToOpenSession: ICReturn.Code](icreturn/devicefailedtoopensession.md)
  Failed to open a session on a specified device.
- [static var deviceFailedToSendData: ICReturn.Code](icreturn/devicefailedtosenddata.md)
  Failed to send data.
- [static var deviceFailedToTakePicture: ICReturn.Code](icreturn/devicefailedtotakepicture.md)
  Failed to take a tethered-capture picture on a camera device.
- [static var deviceIsBusyEnumerating: ICReturn.Code](icreturn/deviceisbusyenumerating.md)
  The device is currently enumerating assets.
- [static var deviceIsPasscodeLocked: ICReturn.Code](icreturn/deviceispasscodelocked.md)
  The device is locked with a passcode. Its contents cannot be seen unless it is unlocked.
- [static var deviceNeedsCredentials: ICReturn.Code](icreturn/deviceneedscredentials.md)
  The device reports credentials are required to open the device.
- [static var deviceSoftwareInstallationCanceled: ICReturn.Code](icreturn/devicesoftwareinstallationcanceled.md)
  Software installation for the device has been canceled.
- [static var deviceSoftwareInstallationCompleted: ICReturn.Code](icreturn/devicesoftwareinstallationcompleted.md)
  Software installation for the device has completed successfully.
- [static var deviceSoftwareInstallationFailed: ICReturn.Code](icreturn/devicesoftwareinstallationfailed.md)
  Software installation for the device failed.
- [static var deviceSoftwareIsBeingInstalled: ICReturn.Code](icreturn/devicesoftwareisbeinginstalled.md)
  Failed to open session because software to communicate with the device is being installed.
- [static var deviceSoftwareNotAvailable: ICReturn.Code](icreturn/devicesoftwarenotavailable.md)
  Software for the device is not available from Apple.
- [static var deviceSoftwareNotInstalled: ICReturn.Code](icreturn/devicesoftwarenotinstalled.md)
  Failed to open session because software to communicate with the device is not installed.
- [static var downloadCanceled: ICReturn.Code](icreturn/downloadcanceled.md)
  A download operation was canceled.
- [static var downloadFailed: ICReturn.Code](icreturn/downloadfailed.md)
  A non-specific error occurred while downloading a file.
- [static var errorDomain: String](icreturn/errordomain.md)
- [static var exFATVolumeInvalid: ICReturn.Code](icreturn/exfatvolumeinvalid.md)
  EXFAT volume is invalid, and cannot be enumerated.
- [static var failedToCompletePassThroughCommand: ICReturn.Code](icreturn/failedtocompletepassthroughcommand.md)
  Failed to complete a pass-through (e.g., PTP pass-through) command.
- [static var failedToCompleteSendMessageRequest: ICReturn.Code](icreturn/failedtocompletesendmessagerequest.md)
  A request to send a message to a device failed.
- [static var failedToDisabeTethering: ICReturn.Code](icreturn/failedtodisabetethering.md)
  A request to send a message to a device failed.
- [static var failedToEnabeTethering: ICReturn.Code](icreturn/failedtoenabetethering.md)
  Failed to enable tethered-capture on a camera device.
- [static var invalidParam: ICReturn.Code](icreturn/invalidparam.md)
  An invalid parameter was found.
- [static var multiErrorDictionary: ICReturn.Code](icreturn/multierrordictionary.md)
  Multierror
- [static var receivedUnsolicitedScannerErrorInfo: ICReturn.Code](icreturn/receivedunsolicitedscannererrorinfo.md)
  An unsolicited error information was received from a scanner.
- [static var receivedUnsolicitedScannerStatusInfo: ICReturn.Code](icreturn/receivedunsolicitedscannerstatusinfo.md)
  An unsolicited status information was received from a scanner.
- [static var scanOperationCanceled: ICReturn.Code](icreturn/scanoperationcanceled.md)
  The scan operation is canceled.
- [static var scannerFailedToCompleteOverviewScan: ICReturn.Code](icreturn/scannerfailedtocompleteoverviewscan.md)
  Overview scan operation failed to complete on the specified scanner.
- [static var scannerFailedToCompleteScan: ICReturn.Code](icreturn/scannerfailedtocompletescan.md)
  Scan operation failed to complete on the specified scanner.
- [static var scannerFailedToSelectFunctionalUnit: ICReturn.Code](icreturn/scannerfailedtoselectfunctionalunit.md)
  Failed to select a functional unit on the specified scanner.
- [static var scannerInUseByLocalUser: ICReturn.Code](icreturn/scannerinusebylocaluser.md)
  Scanner is being used by a local user.
- [static var scannerInUseByRemoteUser: ICReturn.Code](icreturn/scannerinusebyremoteuser.md)
  Scanner is being used by a remote user.
- [static var sessionNotOpened: ICReturn.Code](icreturn/sessionnotopened.md)
  Session is not open.
- [static var success: ICReturn.Code](icreturn/success.md)
  Operation successful.
- [static var uploadFailed: ICReturn.Code](icreturn/uploadfailed.md)
  A non-specific error occurred while updownloading a file.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ICLegacyReturn](iclegacyreturn.md)
- [struct ICReturnConnectionError](icreturnconnectionerror.md)
  A connection error returned from ImageCaptureCore.
- [struct ICReturnDownloadError](icreturndownloaderror.md)
  A download error returned from ImageCaptureCore.
- [struct ICReturnMetadataError](icreturnmetadataerror.md)
  A metadata error returned from ImageCaptureCore.
- [struct ICReturnObjectError](icreturnobjecterror.md)
  An object error returned from ImageCaptureCore.
- [struct ICReturnPTPDeviceError](icreturnptpdeviceerror.md)
  A PTP device error returned from ImageCaptureCore.
- [struct ICReturnThumbnailError](icreturnthumbnailerror.md)
  A thumbnail error returned from ImageCaptureCore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icreturn)*