# ICCameraDevice

**Framework**: ImageCaptureCore  
**Kind**: class

An object that represents a camera.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
class ICCameraDevice
```

## Topics

### Reading Files
- [var contents: [ICCameraItem]?](iccameradevice/contents.md)
  All image, movie, and audio files stored on the camera, in an order that reflects the camera’s storage folder structure.
- [var mediaFiles: [ICCameraItem]?](iccameradevice/mediafiles.md)
  All image, movie and audio files stored on the camera, without regard to the camera’s storage folder structure.
- [var contentCatalogPercentCompleted: Int](iccameradevice/contentcatalogpercentcompleted.md)
  The percentage of the camera’s content that has been catalogued.
- [func files(ofType: String) -> [String]?](iccameradevice/files(oftype:).md)
  Returns an array of files of the selected type on the camera.
- [func requestReadData(from: ICCameraFile, atOffset: off_t, length: off_t, readDelegate: Any, didReadDataSelector: Selector, contextInfo: UnsafeMutableRawPointer?)](iccameradevice/requestreaddata(from:atoffset:length:readdelegate:didreaddataselector:contextinfo:).md)
  Asynchronously reads data of a specified length from a specified offset.
### Uploading Files
- [struct ICUploadOption](icuploadoption.md)
  An option for uploading a file to the camera.
- [func requestUploadFile(URL, options: [ICUploadOption : Any], uploadDelegate: Any, didUploadSelector: Selector, contextInfo: UnsafeMutableRawPointer?)](iccameradevice/requestuploadfile(_:options:uploaddelegate:diduploadselector:contextinfo:).md)
  Uploads a file to the camera.
### Downloading Files
- [struct ICDownloadOption](icdownloadoption.md)
  An option for downloading a file from the camera.
- [func cancelDownload()](iccameradevice/canceldownload.md)
  Cancels a download from the camera.
- [func requestDownloadFile(ICCameraFile, options: [ICDownloadOption : Any], downloadDelegate: any ICCameraDeviceDownloadDelegate, didDownloadSelector: Selector, contextInfo: UnsafeMutableRawPointer?)](iccameradevice/requestdownloadfile(_:options:downloaddelegate:diddownloadselector:contextinfo:).md)
  Downloads a file from the camera.
- [protocol ICCameraDeviceDownloadDelegate](iccameradevicedownloaddelegate.md)
  Methods for managing camera file downloads.
### Deleting Files
- [var isLocked: Bool](iccameradevice/islocked.md)
  A Boolean value indicating whether the device is locked, preventing deletion of any asset.
- [struct ICDeleteResult](icdeleteresult.md)
  The result of a deletion request.
- [struct ICDeleteError](icdeleteerror.md)
  An error resulting from a deletion request.
- [func requestDeleteFiles([ICCameraItem])](iccameradevice/requestdeletefiles(_:).md)
  Deletes files from the camera.
- [func requestDeleteFiles([ICCameraItem], deleteFailed: ([ICDeleteError : ICCameraItem]) -> Void, completion: ([ICDeleteResult : [ICCameraItem]], (any Error)?) -> Void) -> Progress?](iccameradevice/requestdeletefiles(_:deletefailed:completion:).md)
  Deletes files from the camera, with the ability to catch failures and execute a completion block.
- [func cancelDelete()](iccameradevice/canceldelete.md)
  Cancels the current delete operation.
### Taking Pictures
- [var tetheredCaptureEnabled: Bool](iccameradevice/tetheredcaptureenabled.md)
  A Boolean value indicating whether tethered capture is enabled on the camera.
- [var ptpEventHandler: (Data) -> Void](iccameradevice/ptpeventhandler.md)
  A closure for handling PTP event packets.
- [func requestEnableTethering()](iccameradevice/requestenabletethering.md)
  Enables tethered capture if the camera has the capability to take pictures while connected.
- [func requestTakePicture()](iccameradevice/requesttakepicture.md)
  Captures a new image using the camera.
- [func requestSendPTPCommand(Data, outData: Data?, sendCommandDelegate: Any, didSendCommand: Selector, contextInfo: UnsafeMutableRawPointer?)](iccameradevice/requestsendptpcommand(_:outdata:sendcommanddelegate:didsendcommand:contextinfo:).md)
  Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.
- [func requestSendPTPCommand(Data, outData: Data?, completion: (Data, Data, (any Error)?) -> Void)](iccameradevice/requestsendptpcommand(_:outdata:completion:).md)
  Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.
- [func requestDisableTethering()](iccameradevice/requestdisabletethering.md)
  Disables tethered capture on the camera.
### Inspecting the Battery Charge Level
- [var batteryLevelAvailable: Bool](iccameradevice/batterylevelavailable.md)
  A Boolean value that indicates whether the battery charge level is available.
- [var batteryLevel: Int](iccameradevice/batterylevel.md)
  The battery charge level.
### Synchronizing the Clock
- [var timeOffset: TimeInterval](iccameradevice/timeoffset.md)
  The time offset, in seconds, between the camera’s clock and the computer’s clock.
- [func requestSyncClock()](iccameradevice/requestsyncclock.md)
  Synchronizes the camera’s clock with the computer’s clock.
### Detecting Apple Devices
- [var isAccessRestrictedAppleDevice: Bool](iccameradevice/isaccessrestrictedappledevice.md)
  A Boolean value indicating whether the device is an Apple device, passcode-locked, and connected to an untrusted host.
- [var iCloudPhotosEnabled: Bool](iccameradevice/icloudphotosenabled.md)
  A Boolean value indicating whether the iCloud Photo Library is enabled on the device.
### Detecting Mass Storage Devices
- [var mountPoint: String?](iccameradevice/mountpoint.md)
  The file system mount point for a camera using the mass storage transport type.
### Removing a Device
- [var isEjectable: Bool](iccameradevice/isejectable.md)
  A Boolean value indicating whether the device can be ‘soft’ removed or disconnected.
### Instance Properties
- [var mediaPresentation: ICMediaPresentation](iccameradevice/mediapresentation.md)

## Relationships

### Inherits From
- [ICDevice](icdevice.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol ICCameraDeviceDelegate](iccameradevicedelegate.md)
  Methods for detecting cameras, getting metadata and thumbnails, handling access and capability changes, and performing other actions on connected cameras.
- [class ICCameraItem](iccameraitem.md)
  An abstract class that represents a camera item.
- [class ICCameraFile](iccamerafile.md)
  An object that represents a file on a camera.
- [class ICCameraFolder](iccamerafolder.md)
  An object that represents a folder on a camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice)*