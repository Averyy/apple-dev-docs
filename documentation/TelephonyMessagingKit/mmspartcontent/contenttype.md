# contentType

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The content type of the part, as a Uniform Type Identifier.

**Availability**:
- iOS 26.0+

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

You can also use custom content types, such as a [`UTType`](../../UniformTypeIdentifiers/uttype-swift.struct.md) based on a custom MIME type.

## See Also

### Accessing part properties
- [var data: Data](./data.md)
  The raw data used for the MMS content part.
- [var disposition: MMSPartContent.MMSDispositionType](./disposition.md)
  The disposition of the MMS part, indicating whether the part renders inline or as an attachment.
- [MMSPartContent.MMSDispositionType](./mmsdispositiontype.md)
  A structure that defines the disposition of the content part when rendered.
- [var filename: String](./filename.md)
  The file name of the MMS part.
- [var contentID: String](./contentid.md)
  A unique identifier for the part.
- [struct UTType](../../UniformTypeIdentifiers/uttype-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent/contenttype)*