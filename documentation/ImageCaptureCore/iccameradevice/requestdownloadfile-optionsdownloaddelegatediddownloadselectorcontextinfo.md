# requestDownloadFile(_:options:downloadDelegate:didDownloadSelector:contextInfo:)

**Framework**: ImageCaptureCore  
**Kind**: method

Downloads a file from the camera.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func requestDownloadFile(_ file: ICCameraFile, options: [ICDownloadOption : Any] = [:], downloadDelegate: any ICCameraDeviceDownloadDelegate, didDownloadSelector selector: Selector, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

Once this request completes, [`didDownloadFile(_:error:options:contextInfo:)`](iccameradevicedownloaddelegate/diddownloadfile(_:error:options:contextinfo:).md) is called on the `downloadDelegate`.

## See Also

- [struct ICDownloadOption](icdownloadoption.md)
  An option for downloading a file from the camera.
- [func cancelDownload()](iccameradevice/canceldownload.md)
  Cancels a download from the camera.
- [protocol ICCameraDeviceDownloadDelegate](iccameradevicedownloaddelegate.md)
  Methods for managing camera file downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/requestdownloadfile(_:options:downloaddelegate:diddownloadselector:contextinfo:))*