# ICDownloadOption

**Framework**: ImageCaptureCore  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * ICDownloadOption;
```

## Topics

### Download Options
- [static let downloadsDirectoryURL: ICDownloadOption](./icdownloadoption/downloadsdirectoryurl.md)
  A writable directory where the downloaded files should be saved.
- [static let saveAsFilename: ICDownloadOption](./icdownloadoption/saveasfilename.md)
  The name to be used for the downloaded file.
- [static let savedFilename: ICDownloadOption](./icdownloadoption/savedfilename.md)
  The actual name of the saved file.
- [static let savedAncillaryFiles: ICDownloadOption](./icdownloadoption/savedancillaryfiles.md)
  An array of files associated with the file being downloaded.
- [static let overwrite: ICDownloadOption](./icdownloadoption/overwrite.md)
  A Boolean value indicating whether the downloaded file should overwrite an existing file with the same name and extension.
- [static let deleteAfterSuccessfulDownload: ICDownloadOption](./icdownloadoption/deleteaftersuccessfuldownload.md)
  A Boolean value indicating whether to delete the file from the device after a successful download.
- [static let sidecarFiles: ICDownloadOption](./icdownloadoption/sidecarfiles.md)
  A Boolean value indicating whether to download all sidecar files along with the media file.
### Initializers
- [init(rawValue: String)](./icdownloadoption/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Downloading Files
- [func cancelDownload()](./iccameradevice/canceldownload%28%29.md)
  Cancels a download from the camera.
- [func requestDownloadFile(ICCameraFile, options: [ICDownloadOption : Any], downloadDelegate: any ICCameraDeviceDownloadDelegate, didDownloadSelector: Selector, contextInfo: UnsafeMutableRawPointer?)](./iccameradevice/requestdownloadfile%28_,options,downloaddelegate,diddownloadselector,contextinfo%29.md)
  Downloads a file from the camera.
- [protocol ICCameraDeviceDownloadDelegate](./iccameradevicedownloaddelegate.md)
  Methods for managing camera file downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdownloadoption)*