# RCSService.FileDownloadRequest.Metadata

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains download metadata from the content server.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct Metadata
```

#### Overview

You receive this type as the return value from the [`download(_:)`](rcsservice/download(_:).md) method of [`RCSService`](rcsservice.md).

## Topics

### Accessing download request properties
- [let contentType: UTType?](rcsservice/filedownloadrequest/metadata/contenttype.md)
  The content type provided by the content server.
- [let suggestedFileName: String?](rcsservice/filedownloadrequest/metadata/suggestedfilename.md)
  The file name provided by the content server.

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
- [RCSService.FileDownloadRequest](rcsservice/filedownloadrequest.md)
  A structure that represents an RCS file download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/filedownloadrequest/metadata)*