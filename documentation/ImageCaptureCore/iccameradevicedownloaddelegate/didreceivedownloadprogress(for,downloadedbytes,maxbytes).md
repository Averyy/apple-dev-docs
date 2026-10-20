# didReceiveDownloadProgress(for:downloadedBytes:maxBytes:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Updates the delegate about the status of the download.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
optional func didReceiveDownloadProgress(for file: ICCameraFile, downloadedBytes: off_t, maxBytes: off_t)
```

```objc
- (void) didReceiveDownloadProgressForFile:(ICCameraFile *) file downloadedBytes:(off_t) downloadedBytes maxBytes:(off_t) maxBytes;
```

## See Also

### Responding to Download Status
- [func didDownloadFile(ICCameraFile, error: (any Error)?, options: [String : Any], contextInfo: UnsafeMutableRawPointer?)](./diddownloadfile%28_,error,options,contextinfo%29.md)
  Tells the delegate that the requested download has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedownloaddelegate/didreceivedownloadprogress(for:downloadedbytes:maxbytes:))*