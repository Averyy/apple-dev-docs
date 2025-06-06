# didReceiveDownloadProgress(for:downloadedBytes:maxBytes:)

**Framework**: ImageCaptureCore  
**Kind**: method

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

## See Also

- [func didDownloadFile(ICCameraFile, error: (any Error)?, options: [String : Any], contextInfo: UnsafeMutableRawPointer?)](iccameradevicedownloaddelegate/diddownloadfile(_:error:options:contextinfo:).md)
  Tells the delegate that the requested download has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedownloaddelegate/didreceivedownloadprogress(for:downloadedbytes:maxbytes:))*