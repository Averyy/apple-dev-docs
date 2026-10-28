# thumbnailContentType

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The content type of the thumbnail.

**Availability**:
- iOS 26.0+

## Declaration

```swift
var thumbnailContentType: UTType?
```

## Discussion

If you don’t set this property, the framework infers a content type from the URL.

## See Also

### Accessing upload request properties
- [var cellularServiceID: CellularServiceID](./cellularserviceid.md)
  The service identifier associated with this request.
- [var fileURL: URL](./fileurl.md)
  The URL of the file to upload.
- [var contentType: UTType?](./contenttype.md)
  The content type of the file.
- [var thumbnailURL: URL?](./thumbnailurl.md)
  An optional file URL for a thumbnail image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/fileuploadrequest/thumbnailcontenttype)*