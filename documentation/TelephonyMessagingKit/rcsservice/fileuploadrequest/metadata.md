# RCSService.FileUploadRequest.Metadata

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that contains upload metadata from the content server.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct Metadata
```

#### Overview

You receive this type as the return value from the [`upload(_:)`](../upload%28_%29.md) method of [`RCSService`](../../rcsservice.md).

## Topics

### Accessing upload metadata
- [let transactionID: UUID](./metadata/transactionid.md)
  A transaction identifier for the upload.
- [let fileMetadata: RCSFileTransferMetadata](./metadata/filemetadata.md)
  Metadata for the uploaded file.
- [let thumbnailMetadata: RCSFileTransferMetadata?](./metadata/thumbnailmetadata.md)
  Metadata for the uploaded thumbnail.
- [struct RCSFileTransferMetadata](../../rcsfiletransfermetadata.md)
  A structure that contains metadata about an RCS file transfer.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Transferring files
- [func upload(RCSService.FileUploadRequest) async throws -> RCSService.FileUploadRequest.Metadata](../upload%28_%29.md)
  Uploads a file to the RCS content server.
- [RCSService.FileUploadRequest](../fileuploadrequest.md)
  A structure that represents an RCS file upload request.
- [func download(RCSService.FileDownloadRequest) async throws -> RCSService.FileDownloadRequest.Metadata](../download%28_%29.md)
  Downloads a file from the RCS content server.
- [RCSService.FileDownloadRequest](../filedownloadrequest.md)
  A structure that represents an RCS file download request.
- [RCSService.FileDownloadRequest.Metadata](../filedownloadrequest/metadata.md)
  A structure that contains download metadata from the content server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/fileuploadrequest/metadata)*