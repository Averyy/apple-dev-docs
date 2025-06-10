# RCSService.FileDownloadRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents an RCS file download request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct FileDownloadRequest
```

## Topics

### Creating a download request
- [init(cellularServiceID: CellularServiceID, fileURL: URL, destinationFileURL: URL)](rcsservice/filedownloadrequest/init(cellularserviceid:fileurl:destinationfileurl:).md)
  Creates a download request instance.
### Accessing download request properties
- [var cellularServiceID: CellularServiceID](rcsservice/filedownloadrequest/cellularserviceid.md)
  The service identifier associated with this request.
- [var fileURL: URL](rcsservice/filedownloadrequest/fileurl.md)
  The URL of the file to download.
- [var destinationFileURL: URL](rcsservice/filedownloadrequest/destinationfileurl.md)
  The destination path of the downloaded file.
### Accessing download metadata
- [RCSService.FileDownloadRequest.Metadata](rcsservice/filedownloadrequest/metadata.md)
  A structure that contains download metadata from the content server.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func upload(RCSService.FileUploadRequest) async throws -> RCSService.FileUploadRequest.Metadata](rcsservice/upload(_:).md)
  Uploads a file to the RCS content server.
- [RCSService.FileUploadRequest](rcsservice/fileuploadrequest.md)
  A structure that represents an RCS file upload request.
- [RCSService.FileUploadRequest.Metadata](rcsservice/fileuploadrequest/metadata.md)
  A structure that contains upload metadata from the content server.
- [func download(RCSService.FileDownloadRequest) async throws -> RCSService.FileDownloadRequest.Metadata](rcsservice/download(_:).md)
  Downloads a file from the RCS content server.
- [RCSService.FileDownloadRequest.Metadata](rcsservice/filedownloadrequest/metadata.md)
  A structure that contains download metadata from the content server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/filedownloadrequest)*