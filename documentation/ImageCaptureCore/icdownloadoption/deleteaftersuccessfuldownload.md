# deleteAfterSuccessfulDownload

**Framework**: ImageCaptureCore  
**Kind**: property

A Boolean value indicating whether to delete the file from the device after a successful download.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
static let deleteAfterSuccessfulDownload: ICDownloadOption
```

#### Discussion

Specify this value as an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object.

## See Also

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
- [static let sidecarFiles: ICDownloadOption](icdownloadoption/sidecarfiles.md)
  A Boolean value indicating whether to download all sidecar files along with the media file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdownloadoption/deleteaftersuccessfuldownload)*