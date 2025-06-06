# ICDownloadOption

**Framework**: ImageCaptureCore  
**Kind**: struct

An option for downloading a file from the camera.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
struct ICDownloadOption
```

## Topics

### Download Options
- [static let downloadsDirectoryURL: ICDownloadOption](icdownloadoption/downloadsdirectoryurl.md)
  A writable directory where the downloaded files should be saved.
- [static let saveAsFilename: ICDownloadOption](icdownloadoption/saveasfilename.md)
  The name to be used for the downloaded file.
- [static let savedFilename: ICDownloadOption](icdownloadoption/savedfilename.md)
  The actual name of the saved file.
- [static let savedAncillaryFiles: ICDownloadOption](icdownloadoption/savedancillaryfiles.md)
  An array of files associated with the file being downloaded.
- [static let overwrite: ICDownloadOption](icdownloadoption/overwrite.md)
  A Boolean value indicating whether the downloaded file should overwrite an existing file with the same name and extension.
- [static let deleteAfterSuccessfulDownload: ICDownloadOption](icdownloadoption/deleteaftersuccessfuldownload.md)
  A Boolean value indicating whether to delete the file from the device after a successful download.
- [static let sidecarFiles: ICDownloadOption](icdownloadoption/sidecarfiles.md)
  A Boolean value indicating whether to download all sidecar files along with the media file.
### Initializers
- [init(rawValue: String)](icdownloadoption/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func cancelDownload()](iccameradevice/canceldownload.md)
  Cancels a download from the camera.
- [func requestDownloadFile(ICCameraFile, options: [ICDownloadOption : Any], downloadDelegate: any ICCameraDeviceDownloadDelegate, didDownloadSelector: Selector, contextInfo: UnsafeMutableRawPointer?)](iccameradevice/requestdownloadfile(_:options:downloaddelegate:diddownloadselector:contextinfo:).md)
  Downloads a file from the camera.
- [protocol ICCameraDeviceDownloadDelegate](iccameradevicedownloaddelegate.md)
  Methods for managing camera file downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdownloadoption)*