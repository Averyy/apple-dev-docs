# RCSService.FileUploadRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents an RCS file upload request.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct FileUploadRequest
```

## Topics

### Creating a file upload request
- [init(cellularServiceID: CellularServiceID, fileURL: URL, contentType: UTType?, thumbnailURL: URL?, thumbnailContentType: UTType?)](./fileuploadrequest/init%28cellularserviceid,fileurl,contenttype,thumbnailurl,thumbnailcontenttype%29.md)
  Creates a new file upload request with the given parameters.
### Accessing upload request properties
- [var cellularServiceID: CellularServiceID](./fileuploadrequest/cellularserviceid.md)
  The service identifier associated with this request.
- [var fileURL: URL](./fileuploadrequest/fileurl.md)
  The URL of the file to upload.
- [var contentType: UTType?](./fileuploadrequest/contenttype.md)
  The content type of the file.
- [var thumbnailURL: URL?](./fileuploadrequest/thumbnailurl.md)
  An optional file URL for a thumbnail image.
- [var thumbnailContentType: UTType?](./fileuploadrequest/thumbnailcontenttype.md)
  The content type of the thumbnail.
### Accessing upload metadata
- [RCSService.FileUploadRequest.Metadata](./fileuploadrequest/metadata.md)
  A structure that contains upload metadata from the content server.
### Supporting RCS encryption
- [var isEndToEndEncrypted: Bool](./fileuploadrequest/isendtoendencrypted.md)
  A Boolean value indicating whether this request should be end-to-end encrypted. If the service does not support end-to-end encryption, the operation will throw [`RCSService.Error.endToEndEncryptionNotSupported`](./error/endtoendencryptionnotsupported.md).

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Transferring files
- [func upload(RCSService.FileUploadRequest) async throws -> RCSService.FileUploadRequest.Metadata](./upload%28_%29.md)
  Uploads a file to the RCS content server.
- [RCSService.FileUploadRequest.Metadata](./fileuploadrequest/metadata.md)
  A structure that contains upload metadata from the content server.
- [func download(RCSService.FileDownloadRequest) async throws -> RCSService.FileDownloadRequest.Metadata](./download%28_%29.md)
  Downloads a file from the RCS content server.
- [RCSService.FileDownloadRequest](./filedownloadrequest.md)
  A structure that represents an RCS file download request.
- [RCSService.FileDownloadRequest.Metadata](./filedownloadrequest/metadata.md)
  A structure that contains download metadata from the content server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/fileuploadrequest)*