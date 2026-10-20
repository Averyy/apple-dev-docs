# cancelDownload()

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Cancels a download from the camera.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func cancelDownload()
```

```objc
- (void) cancelDownload;
```

## See Also

### Downloading Files
- [struct ICDownloadOption](../icdownloadoption.md)
  An option for downloading a file from the camera.
- [func requestDownloadFile(ICCameraFile, options: [ICDownloadOption : Any], downloadDelegate: any ICCameraDeviceDownloadDelegate, didDownloadSelector: Selector, contextInfo: UnsafeMutableRawPointer?)](./requestdownloadfile%28_,options,downloaddelegate,diddownloadselector,contextinfo%29.md)
  Downloads a file from the camera.
- [protocol ICCameraDeviceDownloadDelegate](../iccameradevicedownloaddelegate.md)
  Methods for managing camera file downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/canceldownload())*