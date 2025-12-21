# download(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Downloads a file from the RCS content server.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final func download(_ downloadRequest: RCSService.FileDownloadRequest) async throws -> RCSService.FileDownloadRequest.Metadata
```

#### Return Value

A [`RCSService.FileDownloadRequest.Metadata`](rcsservice/filedownloadrequest/metadata.md) instance that contains information about the downloaded file.

#### Discussion

Call this method after receiving an [`RCSMessage`](rcsmessage.md) whose content type is [`RCSMessage.Content.fileTransfer(_:)`](rcsmessage/content-swift.enum/filetransfer(_:).md) from the RCS service’s [`incomingMessageNotifications`](rcsservice/incomingmessagenotifications.md) asynchronous sequence. Use the message’s [`fileMetadata`](rcsmessage/filetransfer/filemetadata.md) and optional [`thumbnailMetadata`](rcsmessage/filetransfer/thumbnailmetadata.md), both of type [`RCSFileTransferMetadata`](rcsfiletransfermetadata.md), to get the URLs to download. The metadata structure also contains other properties which may be useful for downloading, such as the file size and type.

The following example assumes you received a [`RCSMessage.FileTransfer`](rcsmessage/filetransfer.md) instance called `fileTransferMessage` from the incoming message notifications sequence. It uses the message’s metadata to get a URL with which to call `download(_:)`, and then uses metadata from the download to get a [`suggestedFileName`](rcsservice/filedownloadrequest/metadata/suggestedfilename.md) to help place the file in a permanent location.

```swift
let service = TelephonyMessagingSession.shared.rcsService

let cellularServices = try TelephonyMessagingSession.shared.cellularServices
let cellularServiceID = cellularServices[0].id

guard service.isViable(for: cellularServiceID) else { return }

let downloadURL = fileTransferMessage.fileMetadata.url
let temporaryURL = URL.temporaryDirectory
    .appendingPathComponent(downloadURL.lastPathComponent)

// Download file.
let request = RCSService.FileDownloadRequest(cellularServiceID: cellularServiceID,
                                             fileURL: downloadURL,
                                             destinationFileURL: temporaryURL)
let downloadMetadata = try await service.download(request)

// Move file to permanent location, using suggested file name.
let receivedURL = URL.documentsDirectory
    .appendingPathComponent(downloadMetadata.suggestedFileName ?? "Unknown")
try FileManager.default.moveItem(at: temporaryURL,
                                 to: receivedURL)
```

## Parameters

- `downloadRequest`: A   that indicates the URL to download and its destination path on the local filesystem.

## See Also

- [func upload(RCSService.FileUploadRequest) async throws -> RCSService.FileUploadRequest.Metadata](rcsservice/upload(_:).md)
  Uploads a file to the RCS content server.
- [RCSService.FileUploadRequest](rcsservice/fileuploadrequest.md)
  A structure that represents an RCS file upload request.
- [RCSService.FileUploadRequest.Metadata](rcsservice/fileuploadrequest/metadata.md)
  A structure that contains upload metadata from the content server.
- [RCSService.FileDownloadRequest](rcsservice/filedownloadrequest.md)
  A structure that represents an RCS file download request.
- [RCSService.FileDownloadRequest.Metadata](rcsservice/filedownloadrequest/metadata.md)
  A structure that contains download metadata from the content server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/download(_:))*