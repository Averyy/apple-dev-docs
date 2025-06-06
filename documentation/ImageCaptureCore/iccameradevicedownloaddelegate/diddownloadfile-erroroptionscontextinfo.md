# didDownloadFile(_:error:options:contextInfo:)

**Framework**: ImageCaptureCore  
**Kind**: method

Tells the delegate that the requested download has completed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
optional func didDownloadFile(_ file: ICCameraFile, error: (any Error)?, options: [String : Any] = [:], contextInfo: UnsafeMutableRawPointer?)
```

## See Also

- [func didReceiveDownloadProgress(for: ICCameraFile, downloadedBytes: off_t, maxBytes: off_t)](iccameradevicedownloaddelegate/didreceivedownloadprogress(for:downloadedbytes:maxbytes:).md)
  Updates the delegate about the status of the download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedownloaddelegate/diddownloadfile(_:error:options:contextinfo:))*