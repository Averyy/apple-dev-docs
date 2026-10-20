# ICCameraDeviceDownloadDelegate

**Framework**: ImageCaptureCore  
**Kind**: protocol  
**Role**: Protocol

Methods for managing camera file downloads.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
protocol ICCameraDeviceDownloadDelegate : NSObjectProtocol
```

```objc
@protocol ICCameraDeviceDownloadDelegate <NSObject>
```

## Topics

### Responding to Download Status
- [func didDownloadFile(ICCameraFile, error: (any Error)?, options: [String : Any], contextInfo: UnsafeMutableRawPointer?)](./iccameradevicedownloaddelegate/diddownloadfile%28_,error,options,contextinfo%29.md)
  Tells the delegate that the requested download has completed.
- [func didReceiveDownloadProgress(for: ICCameraFile, downloadedBytes: off_t, maxBytes: off_t)](./iccameradevicedownloaddelegate/didreceivedownloadprogress%28for,downloadedbytes,maxbytes%29.md)
  Updates the delegate about the status of the download.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Downloading Files
- [struct ICDownloadOption](./icdownloadoption.md)
  An option for downloading a file from the camera.
- [func cancelDownload()](./iccameradevice/canceldownload%28%29.md)
  Cancels a download from the camera.
- [func requestDownloadFile(ICCameraFile, options: [ICDownloadOption : Any], downloadDelegate: any ICCameraDeviceDownloadDelegate, didDownloadSelector: Selector, contextInfo: UnsafeMutableRawPointer?)](./iccameradevice/requestdownloadfile%28_,options,downloaddelegate,diddownloadselector,contextinfo%29.md)
  Downloads a file from the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedownloaddelegate)*