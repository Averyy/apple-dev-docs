# contentType

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The content type of the file.

**Availability**:
- iOS 26.0+

## Declaration

```swift
var contentType: UTType?
```

## Discussion

If you don’t set this property, the framework infers a content type from the URL.

## See Also

### Accessing upload request properties
- [var cellularServiceID: CellularServiceID](./cellularserviceid.md)
  The service identifier associated with this request.
- [var fileURL: URL](./fileurl.md)
  The URL of the file to upload.
- [var thumbnailURL: URL?](./thumbnailurl.md)
  An optional file URL for a thumbnail image.
- [var thumbnailContentType: UTType?](./thumbnailcontenttype.md)
  The content type of the thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/fileuploadrequest/contenttype)*