# savedFilename

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Type Property

The actual name of the saved file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
static let savedFilename: ICDownloadOption
```

```c
extern ICDownloadOption const ICSavedFilename;
```

## Discussion

The options dictionary returned in [`didDownloadFile(_:error:options:contextInfo:)`](../iccameradevicedownloaddelegate/diddownloadfile%28_,error,options,contextinfo%29.md) will have this key.

## See Also

### Download Options
- [static let downloadsDirectoryURL: ICDownloadOption](./downloadsdirectoryurl.md)
  A writable directory where the downloaded files should be saved.
- [static let saveAsFilename: ICDownloadOption](./saveasfilename.md)
  The name to be used for the downloaded file.
- [static let savedAncillaryFiles: ICDownloadOption](./savedancillaryfiles.md)
  An array of files associated with the file being downloaded.
- [static let overwrite: ICDownloadOption](./overwrite.md)
  A Boolean value indicating whether the downloaded file should overwrite an existing file with the same name and extension.
- [static let deleteAfterSuccessfulDownload: ICDownloadOption](./deleteaftersuccessfuldownload.md)
  A Boolean value indicating whether to delete the file from the device after a successful download.
- [static let sidecarFiles: ICDownloadOption](./sidecarfiles.md)
  A Boolean value indicating whether to download all sidecar files along with the media file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdownloadoption/savedfilename)*