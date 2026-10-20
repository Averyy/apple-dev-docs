# RCSService.FileDownloadRequest.Metadata

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that contains download metadata from the content server.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct Metadata
```

#### Overview

You receive this type as the return value from the [`download(_:)`](../download%28_%29.md) method of [`RCSService`](../../rcsservice.md).

## Topics

### Accessing download request properties
- [let contentType: UTType?](./metadata/contenttype.md)
  The content type provided by the content server.
- [let suggestedFileName: String?](./metadata/suggestedfilename.md)
  The file name provided by the content server.

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
- [RCSService.FileUploadRequest.Metadata](../fileuploadrequest/metadata.md)
  A structure that contains upload metadata from the content server.
- [func download(RCSService.FileDownloadRequest) async throws -> RCSService.FileDownloadRequest.Metadata](../download%28_%29.md)
  Downloads a file from the RCS content server.
- [RCSService.FileDownloadRequest](../filedownloadrequest.md)
  A structure that represents an RCS file download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/filedownloadrequest/metadata)*