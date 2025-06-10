# init(cellularServiceID:fileURL:contentType:thumbnailURL:thumbnailContentType:)

**Framework**: TelephonyMessagingKit  
**Kind**: init

Creates a new file upload request with the given parameters.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
init(cellularServiceID: CellularServiceID, fileURL: URL, contentType: UTType? = nil, thumbnailURL: URL? = nil, thumbnailContentType: UTType? = nil)
```

## Parameters

- `cellularServiceID`: The service identifier associated with this request.
- `fileURL`: The URL of the file to upload.
- `contentType`: The content type of the file.
- `thumbnailURL`: An optional file URL for a thumbnail image.
- `thumbnailContentType`: The content type of the thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/fileuploadrequest/init(cellularserviceid:fileurl:contenttype:thumbnailurl:thumbnailcontenttype:))*