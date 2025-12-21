# contentType

**Framework**: TelephonyMessagingKit  
**Kind**: property

The content type of the part, as a Uniform Type Identifier.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
var contentType: UTType?
```

#### Discussion

Most MMS clients support the following content types:

- `text/x-vcalendar`
- `text/vcalendar`
- `text/x-calendar`
- `text/calendar`
- `text/x-vlocation`
- `text/x-location`
- `text/x-vcard`
- `text/vcard`
- `text/plain`
- `image/jpg`
- `image/bmp`
- `image/x-bmp`
- `image/png`
- `image/gif`
- `audio/x-aac`
- `audio/aac`
- `video/3gp`
- `video/3gp`

You can also use custom content types, such as a [`UTType`](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTType-swift.struct) based on a custom MIME type.

## See Also

- [var data: Data](mmspartcontent/data.md)
  The raw data used for the MMS content part.
- [var disposition: MMSPartContent.MMSDispositionType](mmspartcontent/disposition.md)
  The disposition of the MMS part, indicating whether the part renders inline or as an attachment.
- [MMSPartContent.MMSDispositionType](mmspartcontent/mmsdispositiontype.md)
  A structure that defines the disposition of the content part when rendered.
- [var filename: String](mmspartcontent/filename.md)
  The file name of the MMS part.
- [var contentID: String](mmspartcontent/contentid.md)
  A unique identifier for the part.
- [struct UTType](../UniformTypeIdentifiers/UTType-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent/contenttype)*