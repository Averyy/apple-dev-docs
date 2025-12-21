# upload(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Uploads a file to the RCS content server.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final func upload(_ uploadRequest: RCSService.FileUploadRequest) async throws -> RCSService.FileUploadRequest.Metadata
```

#### Return Value

A [`RCSService.FileUploadRequest.Metadata`](rcsservice/fileuploadrequest/metadata.md) instance that contains information about the uploaded file.

#### Discussion

Sending a file to a recipient over RCS is a two-step process:

1. Call `upload(_:)` to upload the file to the carrier.
2. Send a message of type [`RCSMessage.FileTransfer`](rcsmessage/filetransfer.md) to the recipient, using metadata returned from the upload step.

The following example shows this process:

```swift
let service = TelephonyMessagingSession.shared.rcsService

let cellularServices = try TelephonyMessagingSession.shared.cellularServices
let cellularServiceID = cellularServices[0].id

guard service.isViable(for: cellularServiceID) else { return }
guard let uploadURL = URL(string: SAMPLE_UPLOAD_FILE_PATH) else { return }

// Upload file.
let request = RCSService.FileUploadRequest(cellularServiceID: cellularServiceID,
                                                 fileURL: uploadURL,
                                                 contentType: UTType.plainText)
let uploadMetadata = try await service.upload(request)

// Send file transfer message to recipient handle, using upload metadata.
try await service.sendMessage(RCSMessage.FileTransfer(fileMetadata: uploadMetadata.fileMetadata),
                    to: RCSHandle.phoneNumber(SAMPLE_PHONE_NUMBER)!,
                    using: cellularServiceID,
                    messageID: RCSMessageID(rawValue: SAMPLE_RCS_MESSAGE_ID))
```

> **Note**:  If RCS file transfer isn’t supported, this method throws [`RCSService.Error.notSupported`](rcsservice/error/notsupported.md). If the file exceeds the maximum size, it throws [`RCSService.Error.maximumSizeExceeded`](rcsservice/error/maximumsizeexceeded.md).

## Parameters

- `uploadRequest`: A   instance that describes the file to upload and an optional thumbnail.

## See Also

- [RCSService.FileUploadRequest](rcsservice/fileuploadrequest.md)
  A structure that represents an RCS file upload request.
- [RCSService.FileUploadRequest.Metadata](rcsservice/fileuploadrequest/metadata.md)
  A structure that contains upload metadata from the content server.
- [func download(RCSService.FileDownloadRequest) async throws -> RCSService.FileDownloadRequest.Metadata](rcsservice/download(_:).md)
  Downloads a file from the RCS content server.
- [RCSService.FileDownloadRequest](rcsservice/filedownloadrequest.md)
  A structure that represents an RCS file download request.
- [RCSService.FileDownloadRequest.Metadata](rcsservice/filedownloadrequest/metadata.md)
  A structure that contains download metadata from the content server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/upload(_:))*