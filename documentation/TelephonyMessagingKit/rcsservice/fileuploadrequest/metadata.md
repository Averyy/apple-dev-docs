# RCSService.FileUploadRequest.Metadata

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains upload metadata from the content server.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct Metadata
```

#### Overview

You receive this type as the return value from the [`upload(_:)`](rcsservice/upload(_:).md) method of [`RCSService`](rcsservice.md).

## Topics

### Accessing upload metadata
- [let transactionID: UUID](rcsservice/fileuploadrequest/metadata/transactionid.md)
  A transaction identifier for the upload.
- [let fileMetadata: RCSFileTransferMetadata](rcsservice/fileuploadrequest/metadata/filemetadata.md)
  Metadata for the uploaded file.
- [let thumbnailMetadata: RCSFileTransferMetadata?](rcsservice/fileuploadrequest/metadata/thumbnailmetadata.md)
  Metadata for the uploaded thumbnail.
- [struct RCSFileTransferMetadata](rcsfiletransfermetadata.md)
  A structure that contains metadata about an RCS file transfer.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func upload(RCSService.FileUploadRequest) async throws -> RCSService.FileUploadRequest.Metadata](rcsservice/upload(_:).md)
  Uploads a file to the RCS content server.
- [RCSService.FileUploadRequest](rcsservice/fileuploadrequest.md)
  A structure that represents an RCS file upload request.
- [func download(RCSService.FileDownloadRequest) async throws -> RCSService.FileDownloadRequest.Metadata](rcsservice/download(_:).md)
  Downloads a file from the RCS content server.
- [RCSService.FileDownloadRequest](rcsservice/filedownloadrequest.md)
  A structure that represents an RCS file download request.
- [RCSService.FileDownloadRequest.Metadata](rcsservice/filedownloadrequest/metadata.md)
  A structure that contains download metadata from the content server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/fileuploadrequest/metadata)*