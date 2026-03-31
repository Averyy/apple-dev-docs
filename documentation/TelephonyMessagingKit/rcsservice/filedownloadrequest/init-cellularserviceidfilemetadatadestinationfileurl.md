# init(cellularServiceID:fileMetadata:destinationFileURL:)

**Framework**: TelephonyMessagingKit  
**Kind**: init

Creates a download request instance.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
init(cellularServiceID: CellularServiceID, fileMetadata: RCSFileTransferMetadata, destinationFileURL: URL)
```

#### Discussion

Use this initializer when downloading end-to-end encrypted files.

## Parameters

- `cellularServiceID`: The service identifier associated with this request.
- `fileMetadata`: The file metadata containing the URL of the file to download.
- `destinationFileURL`: The destination path, including the file name, of the downloaded file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/filedownloadrequest/init(cellularserviceid:filemetadata:destinationfileurl:))*