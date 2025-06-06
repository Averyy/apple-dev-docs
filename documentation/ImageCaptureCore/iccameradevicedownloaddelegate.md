# ICCameraDeviceDownloadDelegate

**Framework**: ImageCaptureCore  
**Kind**: protocol

Methods for managing camera file downloads.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
protocol ICCameraDeviceDownloadDelegate : NSObjectProtocol
```

## Topics

### Responding to Download Status
- [func didDownloadFile(ICCameraFile, error: (any Error)?, options: [String : Any], contextInfo: UnsafeMutableRawPointer?)](iccameradevicedownloaddelegate/diddownloadfile(_:error:options:contextinfo:).md)
  Tells the delegate that the requested download has completed.
- [func didReceiveDownloadProgress(for: ICCameraFile, downloadedBytes: off_t, maxBytes: off_t)](iccameradevicedownloaddelegate/didreceivedownloadprogress(for:downloadedbytes:maxbytes:).md)
  Updates the delegate about the status of the download.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct ICDownloadOption](icdownloadoption.md)
  An option for downloading a file from the camera.
- [func cancelDownload()](iccameradevice/canceldownload.md)
  Cancels a download from the camera.
- [func requestDownloadFile(ICCameraFile, options: [ICDownloadOption : Any], downloadDelegate: any ICCameraDeviceDownloadDelegate, didDownloadSelector: Selector, contextInfo: UnsafeMutableRawPointer?)](iccameradevice/requestdownloadfile(_:options:downloaddelegate:diddownloadselector:contextinfo:).md)
  Downloads a file from the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedownloaddelegate)*