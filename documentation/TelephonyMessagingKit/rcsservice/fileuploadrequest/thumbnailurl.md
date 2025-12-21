# thumbnailURL

**Framework**: TelephonyMessagingKit  
**Kind**: property

An optional file URL for a thumbnail image.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
var thumbnailURL: URL?
```

#### Discussion

The RCS specification limits the thumbnail size to 10KB.

## See Also

- [var cellularServiceID: CellularServiceID](rcsservice/fileuploadrequest/cellularserviceid.md)
  The service identifier associated with this request.
- [var fileURL: URL](rcsservice/fileuploadrequest/fileurl.md)
  The URL of the file to upload.
- [var contentType: UTType?](rcsservice/fileuploadrequest/contenttype.md)
  The content type of the file.
- [var thumbnailContentType: UTType?](rcsservice/fileuploadrequest/thumbnailcontenttype.md)
  The content type of the thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/fileuploadrequest/thumbnailurl)*