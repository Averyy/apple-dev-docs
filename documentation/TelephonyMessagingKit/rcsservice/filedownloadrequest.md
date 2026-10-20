# RCSService.FileDownloadRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents an RCS file download request.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct FileDownloadRequest
```

## Topics

### Creating a download request
- [init(cellularServiceID: CellularServiceID, fileURL: URL, destinationFileURL: URL)](./filedownloadrequest/init%28cellularserviceid,fileurl,destinationfileurl%29.md)
  Creates a download request instance.
- [init(cellularServiceID: CellularServiceID, fileMetadata: RCSFileTransferMetadata, destinationFileURL: URL)](./filedownloadrequest/init%28cellularserviceid,filemetadata,destinationfileurl%29.md)
  Creates a download request instance.
### Accessing download request properties
- [var cellularServiceID: CellularServiceID](./filedownloadrequest/cellularserviceid.md)
  The service identifier associated with this request.
- [var fileURL: URL](./filedownloadrequest/fileurl.md)
  The URL of the file to download.
- [var destinationFileURL: URL](./filedownloadrequest/destinationfileurl.md)
  The destination path of the downloaded file.
### Accessing download metadata
- [RCSService.FileDownloadRequest.Metadata](./filedownloadrequest/metadata.md)
  A structure that contains download metadata from the content server.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Transferring files
- [func upload(RCSService.FileUploadRequest) async throws -> RCSService.FileUploadRequest.Metadata](./upload%28_%29.md)
  Uploads a file to the RCS content server.
- [RCSService.FileUploadRequest](./fileuploadrequest.md)
  A structure that represents an RCS file upload request.
- [RCSService.FileUploadRequest.Metadata](./fileuploadrequest/metadata.md)
  A structure that contains upload metadata from the content server.
- [func download(RCSService.FileDownloadRequest) async throws -> RCSService.FileDownloadRequest.Metadata](./download%28_%29.md)
  Downloads a file from the RCS content server.
- [RCSService.FileDownloadRequest.Metadata](./filedownloadrequest/metadata.md)
  A structure that contains download metadata from the content server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/filedownloadrequest)*