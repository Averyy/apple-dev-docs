# contentID

**Framework**: TelephonyMessagingKit  
**Kind**: property

A unique identifier for the part.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
var contentID: String
```

#### Discussion

You can use this value for ordering or debugging.

## See Also

- [var data: Data](mmspartcontent/data.md)
  The raw data used for the MMS content part.
- [var disposition: MMSPartContent.MMSDispositionType](mmspartcontent/disposition.md)
  The disposition of the MMS part, indicating whether the part renders inline or as an attachment.
- [MMSPartContent.MMSDispositionType](mmspartcontent/mmsdispositiontype.md)
  A structure that defines the disposition of the content part when rendered.
- [var filename: String](mmspartcontent/filename.md)
  The file name of the MMS part.
- [var contentType: UTType?](mmspartcontent/contenttype.md)
  The content type of the part, as a Uniform Type Identifier.
- [struct UTType](../UniformTypeIdentifiers/UTType-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent/contentid)*