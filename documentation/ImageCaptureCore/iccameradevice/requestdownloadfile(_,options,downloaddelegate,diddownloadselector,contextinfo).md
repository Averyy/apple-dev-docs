# requestDownloadFile(_:options:downloadDelegate:didDownloadSelector:contextInfo:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) requestDownloadFile:(ICCameraFile *) file options:(NSDictionary<NSString *,id> *) options downloadDelegate:(id<ICCameraDeviceDownloadDelegate>) downloadDelegate didDownloadSelector:(SEL) selector contextInfo:(void *) contextInfo;
```

#### Discussion

Once this request completes, [`didDownloadFile(_:error:options:contextInfo:)`](../iccameradevicedownloaddelegate/diddownloadfile%28_,error,options,contextinfo%29.md) is called on the `downloadDelegate`.

## See Also

### Downloading Files
- [struct ICDownloadOption](../icdownloadoption.md)
  An option for downloading a file from the camera.
- [func cancelDownload()](./canceldownload%28%29.md)
  Cancels a download from the camera.
- [protocol ICCameraDeviceDownloadDelegate](../iccameradevicedownloaddelegate.md)
  Methods for managing camera file downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/requestdownloadfile(_:options:downloaddelegate:diddownloadselector:contextinfo:))*