# thumbnailURL

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

An optional file URL for a thumbnail image.

**Availability**:
- iOS 26.0+

## Declaration

```swift
var thumbnailURL: URL?
```

## Discussion

The RCS specification limits the thumbnail size to 10KB.

## See Also

### Accessing upload request properties
- [var cellularServiceID: CellularServiceID](./cellularserviceid.md)
  The service identifier associated with this request.
- [var fileURL: URL](./fileurl.md)
  The URL of the file to upload.
- [var contentType: UTType?](./contenttype.md)
  The content type of the file.
- [var thumbnailContentType: UTType?](./thumbnailcontenttype.md)
  The content type of the thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/fileuploadrequest/thumbnailurl)*