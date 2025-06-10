# contentType

**Framework**: TelephonyMessagingKit  
**Kind**: property

The content type of the file.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
var contentType: UTType?
```

#### Discussion

If you don’t set this property, the framework infers a content type from the URL.

## See Also

- [var cellularServiceID: CellularServiceID](rcsservice/fileuploadrequest/cellularserviceid.md)
  The service identifier associated with this request.
- [var fileURL: URL](rcsservice/fileuploadrequest/fileurl.md)
  The URL of the file to upload.
- [var thumbnailURL: URL?](rcsservice/fileuploadrequest/thumbnailurl.md)
  An optional file URL for a thumbnail image.
- [var thumbnailContentType: UTType?](rcsservice/fileuploadrequest/thumbnailcontenttype.md)
  The content type of the thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/fileuploadrequest/contenttype)*