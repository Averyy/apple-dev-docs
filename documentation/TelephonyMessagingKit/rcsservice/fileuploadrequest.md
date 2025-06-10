# RCSService.FileUploadRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents an RCS file upload request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct FileUploadRequest
```

## Topics

### Creating a file upload request
- [init(cellularServiceID: CellularServiceID, fileURL: URL, contentType: UTType?, thumbnailURL: URL?, thumbnailContentType: UTType?)](rcsservice/fileuploadrequest/init(cellularserviceid:fileurl:contenttype:thumbnailurl:thumbnailcontenttype:).md)
  Creates a new file upload request with the given parameters.
### Accessing upload request properties
- [var cellularServiceID: CellularServiceID](rcsservice/fileuploadrequest/cellularserviceid.md)
  The service identifier associated with this request.
- [var fileURL: URL](rcsservice/fileuploadrequest/fileurl.md)
  The URL of the file to upload.
- [var contentType: UTType?](rcsservice/fileuploadrequest/contenttype.md)
  The content type of the file.
- [var thumbnailURL: URL?](rcsservice/fileuploadrequest/thumbnailurl.md)
  An optional file URL for a thumbnail image.
- [var thumbnailContentType: UTType?](rcsservice/fileuploadrequest/thumbnailcontenttype.md)
  The content type of the thumbnail.
### Accessing upload metadata
- [RCSService.FileUploadRequest.Metadata](rcsservice/fileuploadrequest/metadata.md)
  A structure that contains upload metadata from the content server.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func upload(RCSService.FileUploadRequest) async throws -> RCSService.FileUploadRequest.Metadata](rcsservice/upload(_:).md)
  Uploads a file to the RCS content server.
- [RCSService.FileUploadRequest.Metadata](rcsservice/fileuploadrequest/metadata.md)
  A structure that contains upload metadata from the content server.
- [func download(RCSService.FileDownloadRequest) async throws -> RCSService.FileDownloadRequest.Metadata](rcsservice/download(_:).md)
  Downloads a file from the RCS content server.
- [RCSService.FileDownloadRequest](rcsservice/filedownloadrequest.md)
  A structure that represents an RCS file download request.
- [RCSService.FileDownloadRequest.Metadata](rcsservice/filedownloadrequest/metadata.md)
  A structure that contains download metadata from the content server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/fileuploadrequest)*